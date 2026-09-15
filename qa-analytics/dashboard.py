import json
import os
import re
import datetime
from glob import glob
from io import StringIO
from typing import List

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import streamlit as st

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

_LOGO_PATH = os.path.join(os.path.dirname(__file__), "logo.png")

st.set_page_config(
    page_title="DK Fashion – Dashboard Gerencial",
    page_icon=_LOGO_PATH,
    layout="wide",
)

DATA_DIR = os.path.join(os.path.dirname(__file__), "Analytics/data")

REPOS_LANGUAGE = {
    "MarketPlace-Frontend": "ts",
    "MarketPlace-Backend": "ts",
}

SONAR_FILENAME_RE = re.compile(
    r"TPPE-2026\.1-Marketplace-(?P<repo>.+?)-"
    r"(?P<datetime>\d{2}-\d{2}-\d{4}-\d{2}-\d{2}-\d{2})-"
    r"(?P<version>.+)\.json"
)

METRIC_LIST = [
    "files", "functions", "complexity", "comment_lines_density",
    "duplicated_lines_density", "coverage", "ncloc", "tests",
    "test_errors", "test_failures", "test_execution_time", "security_rating",
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def unmarshall(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# SonarQube data loading
# ---------------------------------------------------------------------------

def metric_per_file(json_dict: dict) -> List[dict]:
    result = []
    for component in json_dict.get("components", []):
        ncloc_value = 0
        for measure in component.get("measures", []):
            if measure["metric"] == "ncloc":
                try:
                    ncloc_value = float(measure["value"])
                except (ValueError, KeyError):
                    pass
                break
        qualifier = component.get("qualifier", "")
        if (qualifier == "FIL" and ncloc_value > 0) or qualifier in ("DIR", "UTS"):
            result.append(component)
    return result


def generate_component_df(metrics_list, file_data, lang_ext):
    files_rows, dirs_rows, uts_rows = [], [], []

    for f in file_data:
        qualifier = f.get("qualifier", "")
        row = {m: None for m in metrics_list}
        row["qualifier"] = qualifier
        row["path"] = f.get("path", "")
        for measure in f.get("measures", []):
            if measure["metric"] in metrics_list:
                row[measure["metric"]] = measure.get("value")

        try:
            lang = f.get("language", "")
        except Exception:
            lang = ""

        if qualifier == "FIL" and lang == lang_ext:
            files_rows.append(row)
        elif qualifier == "DIR":
            dirs_rows.append(row)
        elif qualifier == "UTS":
            uts_rows.append(row)

    df = pd.DataFrame(files_rows + dirs_rows + uts_rows)
    return df


@st.cache_data
def load_sonar_data() -> pd.DataFrame:
    # filename: TPPE-2026.1-Marketplace-<Repo>-<datetime>-<version>.json
    sonar_files = glob(os.path.join(DATA_DIR, "TPPE-2026.1-Marketplace-*.json"))
    if not sonar_files:
        return pd.DataFrame()

    frames = []
    for path in sonar_files:
        base = os.path.basename(path)
        match = SONAR_FILENAME_RE.match(base)
        if not match:
            continue
        repo_name = match.group("repo")
        lang_ext = REPOS_LANGUAGE.get(repo_name, "ts")

        raw = unmarshall(path)
        file_data = metric_per_file(raw)
        df = generate_component_df(METRIC_LIST, file_data, lang_ext)
        if df.empty:
            continue

        df["repository"] = repo_name
        df["datetime"] = match.group("datetime")
        df["version"] = match.group("version")
        frames.append(df)

    if not frames:
        return pd.DataFrame()

    result = pd.concat(frames, ignore_index=True)
    result = result.sort_values(by=["repository", "datetime"])
    return result


# ---------------------------------------------------------------------------
# SonarQube metric calculations
# ---------------------------------------------------------------------------

def get_files_df(df):
    fdf = df[df["qualifier"] == "FIL"].copy()
    fdf = fdf.dropna(subset=["functions", "complexity", "comment_lines_density",
                              "duplicated_lines_density", "coverage"])
    return fdf


def get_dir_df(df):
    dirs = df[df["qualifier"] == "DIR"].copy()
    dirs["tests"] = pd.to_numeric(dirs["tests"], errors="coerce")
    if dirs.empty or dirs["tests"].isna().all():
        return None
    return dirs.loc[dirs["tests"].idxmax()]


def get_uts_df(df):
    uts = df[df["qualifier"] == "UTS"].copy()
    uts = uts.fillna(0)
    uts = uts.dropna(subset=["test_execution_time"])
    return uts


def _ncloc(df):
    total = 0
    for val in df.get("ncloc", []):
        try:
            total += int(val)
        except (ValueError, TypeError):
            pass
    return total


def calc_complexity(df):
    fdf = get_files_df(df)
    if fdf.empty:
        return 0
    return len(fdf[(fdf["complexity"].astype(float) / fdf["functions"].astype(float)) < 10]) / len(fdf)


def calc_comments(df):
    fdf = get_files_df(df)
    if fdf.empty:
        return 0
    return len(fdf[(fdf["comment_lines_density"].astype(float) > 10) &
                   (fdf["comment_lines_density"].astype(float) < 30)]) / len(fdf)


def calc_duplication(df):
    fdf = get_files_df(df)
    if fdf.empty:
        return 0
    return len(fdf[fdf["duplicated_lines_density"].astype(float) < 5]) / len(fdf)


def calc_test_success(df):
    dir_row = get_dir_df(df)
    if dir_row is None:
        return 0
    try:
        tests = float(dir_row["tests"])
        errors = float(dir_row["test_errors"])
        failures = float(dir_row["test_failures"])
        if tests == 0:
            return 0
        return (tests - errors - failures) / tests
    except (TypeError, ValueError):
        return 0


def calc_fast_tests(df):
    uts = get_uts_df(df)
    if uts.empty:
        return 0
    return len(uts[uts["test_execution_time"].astype(float) < 300000]) / len(uts)


def calc_coverage(df):
    fdf = get_files_df(df)
    if fdf.empty:
        return 0
    return len(fdf[fdf["coverage"].astype(float) > 60]) / len(fdf)


@st.cache_data
def build_sonar_metrics(sonar_df: pd.DataFrame) -> dict:
    metrics = {}
    for repo in sonar_df["repository"].dropna().unique():
        repo_df = sonar_df[sonar_df["repository"] == repo]
        rows = []
        for dt in repo_df["datetime"].dropna().unique():
            vdf = repo_df[repo_df["datetime"] == dt]
            version = vdf["version"].iloc[0] if not vdf.empty else ""
            rows.append({
                "datetime": dt,
                "version": version,
                "complexity": calc_complexity(vdf),
                "comments": calc_comments(vdf),
                "duplication": calc_duplication(vdf),
                "test_success": calc_test_success(vdf),
                "fast_tests": calc_fast_tests(vdf),
                "coverage": calc_coverage(vdf),
                "ncloc": _ncloc(vdf),
            })

        df = pd.DataFrame(rows)
        # Datetime real (não string) — evita eixo categórico com datas repetidas/embaralhadas
        # entre repositórios diferentes nos gráficos de série temporal.
        df["datetime"] = pd.to_datetime(df["datetime"], format="%m-%d-%Y-%H-%M-%S", errors="coerce")
        df = df.sort_values("datetime").reset_index(drop=True)
        df["code_quality"] = (df["complexity"] * 0.33 + df["comments"] * 0.33 + df["duplication"] * 0.33)
        df["testing_status"] = (df["test_success"] * 0.25 + df["fast_tests"] * 0.25 + df["coverage"] * 0.5)
        df["Maintainability"] = df["code_quality"] * 0.5
        df["Reliability"] = df["testing_status"] * 0.5
        df["total"] = df["Maintainability"] + df["Reliability"]
        metrics[repo] = df

    return metrics


# ---------------------------------------------------------------------------
# Datas de sprint — linhas verticais nos gráficos de qualidade
# ---------------------------------------------------------------------------

SPRINT_START_DATE = "01/09/2026"
SPRINT_END_LIMIT = "30/11/2026"
SPRINT_LENGTH_DAYS = 14


def _sprint_end_dates() -> list:
    """Gera as datas de término de cada sprint (2 semanas), a partir do início do projeto.

    Sprint 1: 01/09 a 14/09 (14 dias, ambos inclusive) — término em 14/09.
    """
    start = pd.to_datetime(SPRINT_START_DATE, dayfirst=True)
    limit = pd.to_datetime(SPRINT_END_LIMIT, dayfirst=True)
    dates = []
    current_end = start + pd.Timedelta(days=SPRINT_LENGTH_DAYS - 1)
    while current_end <= limit:
        dates.append(current_end)
        current_end += pd.Timedelta(days=SPRINT_LENGTH_DAYS)
    return dates


def _quality_rating(value: float) -> tuple:
    """Mapeia um valor [0,1] para um rating estilo SonarCloud (A-E) com cor de semáforo."""
    if value >= 0.8:
        return "A", "#00AA00"
    elif value >= 0.6:
        return "B", "#B0D513"
    elif value >= 0.4:
        return "C", "#EABE06"
    elif value >= 0.2:
        return "D", "#ED7D20"
    else:
        return "E", "#D4333F"


def _add_release_lines(fig: go.Figure) -> go.Figure:
    """Adiciona linhas verticais pontilhadas amarelas marcando o término de cada sprint (2 semanas)."""
    for i, ts in enumerate(_sprint_end_dates(), start=1):
        fig.add_vline(
            x=ts.timestamp() * 1000,
            line_dash="dot",
            line_color="#FFD600",
            annotation_text=f"Sprint {i}",
            annotation_position="top",
        )
    return fig


# ---------------------------------------------------------------------------
# GitHub data loading — API pública (sem token, repos públicos)
# baseado em internal_quality_analysis-github.ipynb
# ---------------------------------------------------------------------------

BUILD_YML_NAME    = "build"
GITHUB_ORG        = "fga-eps-mds"
GITHUB_REPO_PREFIX = "2026.1-MeasureSoftGram-"
GITHUB_API_BASE   = "https://api.github.com"
_GH_HEADERS       = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


def _gh_paginate(url: str, params: dict = None) -> list:
    """Percorre todas as páginas de um endpoint GitHub (Link header)."""
    results = []
    next_url = url
    first = True
    while next_url:
        r = requests.get(
            next_url,
            headers=_GH_HEADERS,
            params={**(params or {}), "per_page": 100} if first else None,
            timeout=15,
        )
        first = False
        r.raise_for_status()
        data = r.json()
        if isinstance(data, list):
            results.extend(data)
        elif isinstance(data, dict):
            results.extend(data.get("workflow_runs", []))
        next_url = None
        for part in r.headers.get("Link", "").split(","):
            if 'rel="next"' in part:
                next_url = part.split(";")[0].strip().strip("<>")
                break
    return results


@st.cache_data(ttl=3600)
def _list_project_repos() -> list:
    """Lista os repos públicos de fga-eps-mds que começam com 2026.1-MeasureSoftGram-."""
    repos = _gh_paginate(f"{GITHUB_API_BASE}/orgs/{GITHUB_ORG}/repos", {"type": "public"})
    return [r["name"] for r in repos if r["name"].startswith(GITHUB_REPO_PREFIX)]


def _get_workflow_data() -> list:
    """Busca workflow runs via GitHub API para todos os repos do projeto."""
    table_data = []
    try:
        repos = _list_project_repos()
    except Exception:
        repos = []
    for repo_name in repos:
        try:
            runs = _gh_paginate(
                f"{GITHUB_API_BASE}/repos/{GITHUB_ORG}/{repo_name}/actions/runs"
            )
            for run in runs:
                try:
                    updated_at = datetime.datetime.strptime(run["updated_at"], "%Y-%m-%dT%H:%M:%SZ")
                    created_at = datetime.datetime.strptime(run["created_at"], "%Y-%m-%dT%H:%M:%SZ")
                    feedback_time = (updated_at - created_at).total_seconds()
                    wf_file = (run.get("path") or "").split("/")[-1]
                    if wf_file.endswith(".yml"):
                        wf_file = wf_file[:-4]
                    table_data.append({
                        "Workflow_run ID": run["id"],
                        "Conclusion": run.get("conclusion"),
                        "Author": (run.get("actor") or {}).get("login", ""),
                        "Created at": created_at,
                        "Updated at": updated_at,
                        "Feedback Time": feedback_time,
                        "Workflow .YML Name": wf_file,
                        "Repository Name": repo_name.split("-")[-1],
                    })
                except Exception:
                    continue
        except Exception:
            continue
    return table_data


def _get_issues_data() -> list:
    """Busca todas as issues (abertas e fechadas) via GitHub API para todos os repos."""
    table_data = []
    try:
        repos = _list_project_repos()
    except Exception:
        repos = []
    for repo_name in repos:
        try:
            issues = _gh_paginate(
                f"{GITHUB_API_BASE}/repos/{GITHUB_ORG}/{repo_name}/issues",
                {"state": "all"},
            )
            for issue in issues:
                if "pull_request" in issue:
                    continue
                table_data.append({
                    "Created at": issue["created_at"],
                    "Closed at": issue.get("closed_at"),
                    "Issue Number": issue["number"],
                    "Issue Title": issue.get("title", ""),
                    "Repository Name": repo_name.split("-")[-1],
                })
        except Exception:
            continue
    return table_data


def ci_feedback_time(df: pd.DataFrame) -> pd.DataFrame:
    """Port de ci_feedback_time() do notebook: filtra workflow 'build' e anota o tempo médio."""
    df_filtered = df[df["Workflow .YML Name"] == BUILD_YML_NAME].copy()
    if df_filtered.empty:
        return df_filtered
    feedback_times = df_filtered["Feedback Time"].tolist()
    avg = sum(feedback_times) / len(feedback_times)
    df_filtered.loc[:, "Ci Feedback Time"] = avg
    return df_filtered


def count_success_failure_workflow_runs(df: pd.DataFrame):
    """Port de count_success_failure_workflow_runs() do notebook."""
    counts = df["Conclusion"].value_counts()
    return counts.get("failure", 0), counts.get("success", 0)


def team_throughput(df: pd.DataFrame, start_date: str, end_date: str):
    """Port de team_throughput() do notebook."""
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)
    df_closed = df[
        (df["Created at"] >= start) &
        (df["Closed at"].notna()) &
        (df["Closed at"] <= end + pd.Timedelta(days=1))
    ]
    df_created = df[df["Created at"] >= start]
    return len(df_closed), len(df_created)


@st.cache_data(ttl=3600)
def load_github_runs() -> pd.DataFrame:
    data = _get_workflow_data()
    return pd.DataFrame(data) if data else pd.DataFrame()


@st.cache_data(ttl=3600)
def load_github_issues() -> pd.DataFrame:
    data = _get_issues_data()
    if not data:
        return pd.DataFrame()
    df = pd.DataFrame(data)
    df["Created at"] = pd.to_datetime(df["Created at"], format="%Y-%m-%dT%H:%M:%SZ", errors="coerce")
    df["Closed at"]  = pd.to_datetime(df["Closed at"],  format="%Y-%m-%dT%H:%M:%SZ", errors="coerce")
    return df


# ---------------------------------------------------------------------------
# Sprint / EVM data (Visão do Gestor)
# ---------------------------------------------------------------------------

SPREADSHEET_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1vEGKl1ZxSeijZwuVfzDAaH6eT9NllpKnPJGDVQK7TP0"
    "/export?format=csv&gid=563726235"
)

_SPRINT_FALLBACK = [
    {"sprint": 1,  "start": "30/03/2026", "end": "06/04/2026", "us_raw": "",            "pp": 0,  "pc": 0,  "ac": 5282.36, "ev": 5282.36,  "pv": 5282.36},
    {"sprint": 2,  "start": "06/04/2026", "end": "13/04/2026", "us_raw": "",            "pp": 0,  "pc": 0,  "ac": 5282.36, "ev": 10564.72, "pv": 10564.72},
    {"sprint": 3,  "start": "13/04/2026", "end": "20/04/2026", "us_raw": "",            "pp": 0,  "pc": 0,  "ac": 5282.36, "ev": 15847.08, "pv": 15847.08},
    {"sprint": 4,  "start": "20/04/2026", "end": "27/04/2026", "us_raw": "",            "pp": 0,  "pc": 0,  "ac": 5282.36, "ev": 21129.44, "pv": 21129.44},
    {"sprint": 5,  "start": "27/04/2026", "end": "04/05/2026", "us_raw": "",            "pp": 0,  "pc": 0,  "ac": 5282.36, "ev": 26411.80, "pv": 10564.72},
    {"sprint": 6,  "start": "04/05/2026", "end": "11/05/2026", "us_raw": "US012; US09", "pp": 34, "pc": 13, "ac": 5282.36, "ev": 31694.16, "pv": 21129.44},
    {"sprint": 7,  "start": "11/05/2026", "end": "18/05/2026", "us_raw": "",            "pp": 0,  "pc": 0,  "ac": 5282.36, "ev": 36976.52, "pv": 31694.16},
    {"sprint": 8,  "start": "18/05/2026", "end": "25/05/2026", "us_raw": "US06; US04",  "pp": 18, "pc": 21, "ac": 5282.36, "ev": 42258.88, "pv": 42258.88},
    {"sprint": 9,  "start": "25/05/2026", "end": "01/06/2026", "us_raw": "US13",        "pp": 21, "pc": 0,  "ac": 5282.36, "ev": 47541.24, "pv": 15847.08},
    {"sprint": 10, "start": "01/06/2026", "end": "08/06/2026", "us_raw": "US15",        "pp": 13, "pc": 0,  "ac": 5282.36, "ev": 52823.60, "pv": 31694.16},
    {"sprint": 11, "start": "08/06/2026", "end": "15/06/2026", "us_raw": "US12",        "pp": 8,  "pc": 0,  "ac": 5282.36, "ev": 58105.96, "pv": 47541.24},
    {"sprint": 12, "start": "15/06/2026", "end": "22/06/2026", "us_raw": "US07",        "pp": 13, "pc": 0,  "ac": 5282.36, "ev": 63388.32, "pv": 63388.32},
    {"sprint": 13, "start": "22/06/2026", "end": "29/06/2026", "us_raw": "US14",        "pp": 21, "pc": 0,  "ac": 5282.36, "ev": 68670.68, "pv": 36976.52},
    {"sprint": 14, "start": "29/06/2026", "end": "06/07/2026", "us_raw": "",            "pp": 0,  "pc": 0,  "ac": 5282.36, "ev": 73953.04, "pv": 73953.04},
]


def _normalize_us_list(us_raw) -> list:
    if not us_raw or str(us_raw).strip() in ("-", "", "nan"):
        return []
    result = []
    for token in re.split(r"[;,\s]+", str(us_raw)):
        m = re.match(r"US(\d+)", token.strip(), re.IGNORECASE)
        if m:
            result.append(f"US{int(m.group(1)):02d}")
    return result


def _parse_brl(val) -> float:
    """Convert Brazilian currency 'R$ 5.282,36' or plain float 5282.36 to float."""
    if isinstance(val, (int, float)):
        return float(val)
    s = str(val).strip()
    if s in ("-", "", "nan") or "planejado" in s.lower():
        return 0.0
    s = re.sub(r"[R$\s]", "", s)
    if "," in s:
        # BR format: '.' = thousands sep, ',' = decimal sep
        s = s.replace(".", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return 0.0


def _assemble_sprint_df(rows: list) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    df["start_date"] = pd.to_datetime(df["start"], format="%d/%m/%Y", errors="coerce")
    df["end_date"]   = pd.to_datetime(df["end"],   format="%d/%m/%Y", errors="coerce")
    df["us_list"] = df["us_raw"].apply(_normalize_us_list)
    for col in ("pp", "pc"):
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
    for col in ("ac", "ev", "pv"):
        df[col] = df[col].apply(_parse_brl)
    return df.reset_index(drop=True)


@st.cache_data(ttl=3600)
def load_sprint_data() -> pd.DataFrame:
    def _norm_col(name: str) -> str:
        return name.replace("\n", " ").strip().lower()

    def _find_col(df, *keywords):
        for col in df.columns:
            normalized = _norm_col(col)
            if all(k.lower() in normalized for k in keywords):
                return col
        return None

    try:
        resp = requests.get(SPREADSHEET_URL, allow_redirects=True, timeout=15)
        resp.raise_for_status()
        content = resp.content.decode("utf-8")
        raw = pd.read_csv(StringIO(content), header=2)

        sprint_col = _find_col(raw, "sprint", "(n)")
        start_col  = _find_col(raw, "in", "cio da sprint") or _find_col(raw, "inicio")
        end_col    = _find_col(raw, "fim da sprint")
        us_col     = _find_col(raw, "us's")
        pp_col     = _find_col(raw, "pontos", "planejados")
        pc_col     = _find_col(raw, "points", "completed")
        ac_col     = _find_col(raw, "actual cost")
        ev_col     = _find_col(raw, "earned value")
        pv_col     = _find_col(raw, "planned value")

        if not all([sprint_col, start_col, end_col]):
            raise ValueError("Colunas obrigatórias não encontradas na planilha")

        col_map = {sprint_col: "sprint", start_col: "start", end_col: "end"}
        for orig, dest in [(us_col, "us_raw"), (pp_col, "pp"), (pc_col, "pc"),
                           (ac_col, "ac"), (ev_col, "ev"), (pv_col, "pv")]:
            if orig:
                col_map[orig] = dest

        df = raw[list(col_map.keys())].rename(columns=col_map).copy()
        df = df[pd.to_numeric(df["sprint"], errors="coerce").notna()].copy()
        df["sprint"] = df["sprint"].astype(int)
        for missing in ("us_raw", "pp", "pc", "ac", "ev", "pv"):
            if missing not in df.columns:
                df[missing] = 0 if missing != "us_raw" else ""
        return _assemble_sprint_df(df.to_dict("records"))

    except Exception:
        return _assemble_sprint_df(_SPRINT_FALLBACK)


@st.cache_data(ttl=3600)
def load_us_github_status() -> dict:
    """Deriva o mapa US→status diretamente de load_github_issues() (dados em tempo real)."""
    df = load_github_issues()
    us_map: dict = {}
    for _, row in df.iterrows():
        m = re.search(r"US(\d+)", str(row.get("Issue Title", "")), re.IGNORECASE)
        if not m:
            continue
        us_key   = f"US{int(m.group(1)):02d}"
        repo     = str(row.get("Repository Name", "Unknown"))
        closed_at = row.get("Closed at")
        closed_str = closed_at.isoformat() if pd.notna(closed_at) else None
        if us_key not in us_map:
            us_map[us_key] = {"repos": [repo], "closed_at": closed_str, "any_open": closed_str is None}
        else:
            if repo not in us_map[us_key]["repos"]:
                us_map[us_key]["repos"].append(repo)
            if closed_str is None:
                us_map[us_key]["any_open"] = True
            elif us_map[us_key]["closed_at"] is not None and closed_str > us_map[us_key]["closed_at"]:
                us_map[us_key]["closed_at"] = closed_str
    return us_map


VELOCITY_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1vEGKl1ZxSeijZwuVfzDAaH6eT9NllpKnPJGDVQK7TP0"
    "/export?format=csv&gid=1057464358"
)


@st.cache_data(ttl=3600)
def load_velocity_data() -> pd.DataFrame:
    """Carrega pontos planejados/concluídos, velocity e velocity mean da planilha."""
    def _parse_float_br(val) -> float:
        if isinstance(val, (int, float)):
            return float(val)
        s = str(val).strip().replace(",", ".")
        try:
            return float(s)
        except ValueError:
            return 0.0

    try:
        resp = requests.get(VELOCITY_URL, allow_redirects=True, timeout=15)
        resp.raise_for_status()
        raw = pd.read_csv(StringIO(resp.content.decode("utf-8")), header=1)
        # Normaliza nomes de colunas para busca flexível
        col_map = {}
        for col in raw.columns:
            norm = col.replace("\n", " ").strip().lower()
            if "sprint" in norm and "(" not in norm:
                col_map[col] = "sprint"
            elif "planejado" in norm or "planned" in norm or "(pp)" in norm:
                col_map[col] = "pp"
            elif "conclu" in norm or "completed" in norm or "(pc)" in norm:
                col_map[col] = "pc"
            elif "mean" in norm or "médio" in norm or "medio" in norm:
                col_map[col] = "velocity_mean"
            elif "velocity" in norm:
                col_map[col] = "velocity"
        df = raw[[c for c in col_map]].rename(columns=col_map)
        df = df[pd.to_numeric(df["sprint"], errors="coerce").notna()].copy()
        df["sprint"] = df["sprint"].astype(int)
        for col in ("pp", "pc", "velocity"):
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)
        df["velocity_mean"] = df["velocity_mean"].apply(_parse_float_br)
        return df.reset_index(drop=True)
    except Exception:
        # Fallback: calcula a partir do sprint_df
        base = load_sprint_data()[["sprint", "pp", "pc"]].copy()
        base["velocity"] = base["pc"].astype(int)
        base["velocity_mean"] = base["pc"].expanding().mean().round(1)
        return base


def build_gantt_df(sprint_df: pd.DataFrame, us_status: dict, today: datetime.date) -> pd.DataFrame:
    # Collect all sprints per US to determine planned start and end
    us_sprints: dict = {}
    for _, row in sprint_df.iterrows():
        for us in row["us_list"]:
            if us not in us_sprints:
                us_sprints[us] = []
            us_sprints[us].append({
                "sprint": int(row["sprint"]),
                "start":  row["start_date"],
                "end":    row["end_date"],
            })

    rows = []
    for us, sprint_list in sorted(us_sprints.items()):
        first  = sprint_list[0]
        last   = sprint_list[-1]
        repos  = ", ".join(us_status.get(us, {}).get("repos", [])) or "N/A"

        plan_start = first["start"]
        plan_end   = last["end"]
        if pd.isna(plan_end):
            plan_end = plan_start + pd.Timedelta(days=7)

        # ── Barra planejada (sempre presente) ────────────────────────────────
        rows.append({
            "US":            us,
            "Início":        plan_start,
            "Fim":           plan_end,
            "Status":        "Planejado",
            "Sprint Inicial": first["sprint"],
            "Repositórios":  repos,
        })

        # ── Barra executada (somente se a sprint já iniciou) ─────────────────
        plan_start_date = plan_start.date() if hasattr(plan_start, "date") else plan_start
        if plan_start_date > today:
            continue  # sprint futura: só mostra o planejado

        gh         = us_status.get(us, {})
        any_open   = gh.get("any_open", True)
        closed_raw = gh.get("closed_at")

        if not any_open and closed_raw:
            exec_status = "Concluído"
            exec_end    = pd.Timestamp(str(closed_raw)[:10])
        else:
            exec_status = "Em Andamento"
            exec_end    = pd.Timestamp(today)

        if pd.isna(exec_end) or exec_end <= plan_start:
            exec_end = plan_start + pd.Timedelta(days=1)

        rows.append({
            "US":            us,
            "Início":        plan_start,
            "Fim":           exec_end,
            "Status":        exec_status,
            "Sprint Inicial": first["sprint"],
            "Repositórios":  repos,
        })

    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------
# ── Tema / CSS global ─────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Destaque na primeira aba (Visão Principal) */
div[data-testid="stTabs"] button[data-baseweb="tab"]:first-of-type {
    background-color: #2B4D6F;
    color: #ffffff !important;
    border-radius: 6px 6px 0 0;
    font-weight: 700;
    padding: 8px 20px;
}
div[data-testid="stTabs"] button[data-baseweb="tab"]:first-of-type:hover {
    background-color: #3a6491;
}
/* Abas inativas */
div[data-testid="stTabs"] button[data-baseweb="tab"] {
    color: #a0b8d0;
}
/* Aba ativa (qualquer) */
div[data-testid="stTabs"] button[data-baseweb="tab"][aria-selected="true"] {
    border-bottom: 3px solid #5f7ea3;
}
/* Cards de métrica */
div[data-testid="metric-container"] {
    background-color: #1a3251;
    border: 1px solid #2B4D6F;
    border-radius: 8px;
    padding: 12px 16px;
}
</style>
""", unsafe_allow_html=True)

sonar_df = load_sonar_data()
sonar_metrics = build_sonar_metrics(sonar_df) if not sonar_df.empty else {}
runs_df = load_github_runs()
issues_df = load_github_issues()
sprint_df = load_sprint_data()
velocity_df = load_velocity_data()
us_status = load_us_github_status()

all_repos_sonar = sorted(sonar_metrics.keys()) if sonar_metrics else []
all_repos_github = sorted(runs_df["Repository Name"].dropna().unique().tolist()) if not runs_df.empty else []

SHOW_TAB_PROCESSO = False

_tabs_labels = ["🔍 Qualidade do Produto"]
if SHOW_TAB_PROCESSO:
    _tabs_labels.insert(0, "⚙️ Processo")
_tabs = st.tabs(_tabs_labels)
tab_qualidade_produto = _tabs[-1]
tab_processo = _tabs[0] if SHOW_TAB_PROCESSO else None

# ---------------------------------------------------------------------------
# TAB – Processo
# ---------------------------------------------------------------------------
if SHOW_TAB_PROCESSO:
    with tab_processo:
        st.subheader("Processo")

        # ── Filtro de Sprint (compartilhado entre Gantt e Velocity) ────────────────
        if not velocity_df.empty:
            v_min = int(velocity_df["sprint"].min())
            v_max = int(velocity_df["sprint"].max())
            v_opts = list(range(v_min, v_max + 1))

            vcol1, vcol2 = st.columns(2)
            with vcol1:
                v_sprint_start = st.selectbox(
                    "Sprint Inicial",
                    options=v_opts, index=0,
                    format_func=lambda x: f"Sprint {x}",
                    key="t1_sprint_start",
                )
            with vcol2:
                v_end_opts = [n for n in v_opts if n >= v_sprint_start]
                v_sprint_end = st.selectbox(
                    "Sprint Final",
                    options=v_end_opts, index=len(v_end_opts) - 1,
                    format_func=lambda x: f"Sprint {x}",
                    key="t1_sprint_end",
                )

        st.markdown("---")

# ---------------------------------------------------------------------------
# TAB – Qualidade do Produto
# ---------------------------------------------------------------------------
with tab_qualidade_produto:
    st.subheader("Qualidade do Produto – SonarCloud")

    # ── Filtro de repositórios ────────────────────────────────────────────────
    selected_sonar_repos = st.multiselect(
        "Repositórios",
        options=all_repos_sonar,
        default=all_repos_sonar,
        key="sonar_repos",
    )
    st.markdown("---")

    if not sonar_metrics:
        st.info("Nenhum dado do SonarCloud encontrado em `data/`.")
    else:
        # ── 1. Cards: qualidade geral atual por repositório (semáforo estilo SonarCloud) ──
        st.markdown("### Qualidade Geral por Repositório")
        quality_cols = st.columns(max(len(selected_sonar_repos), 1))
        for col, repo in zip(quality_cols, selected_sonar_repos):
            df = sonar_metrics.get(repo)
            if df is None or df.empty:
                letter, color = "—", "#5f7ea3"
            else:
                last = df.iloc[-1]
                letter, color = _quality_rating(last["total"])
            col.markdown(f"""
            <div style="text-align:center; padding:14px 8px; background-color:#1a3251;
                        border-radius:10px; border:2px solid {color};">
                <div style="font-size:14px; color:#a0b8d0; margin-bottom:6px;">{repo}</div>
                <div style="font-size:38px; font-weight:800; color:{color}; line-height:1;">{letter}</div>
            </div>
            """, unsafe_allow_html=True)

        legend_items = [
            ("A", "#00AA00", "≥ 80%"),
            ("B", "#B0D513", "60–79%"),
            ("C", "#EABE06", "40–59%"),
            ("D", "#ED7D20", "20–39%"),
            ("E", "#D4333F", "< 20%"),
        ]
        legend_html = "".join(
            f"""<span style="display:inline-flex; align-items:center; margin-right:18px;">
                    <span style="display:inline-block; width:16px; height:16px; border-radius:3px;
                                 background-color:{color}; margin-right:6px;"></span>
                    <span style="color:#a0b8d0; font-size:13px;"><b>{letter}</b> {rng}</span>
                </span>"""
            for letter, color, rng in legend_items
        )
        st.markdown(
            f'<div style="margin-top:4px;">{legend_html}</div>',
            unsafe_allow_html=True,
        )

        st.markdown("---")

        # ── 2. Indicador Total de Qualidade por Repositório ─────────────────────
        st.markdown("### Indicador Total de Qualidade por Repositório")
        fig8 = go.Figure()
        for repo in selected_sonar_repos:
            df = sonar_metrics.get(repo)
            if df is None or df.empty:
                continue
            fig8.add_trace(go.Scatter(
                x=df["datetime"], y=df["total"],
                mode="lines+markers", name=repo,
                hovertemplate="%{x}<br>Total: %{y:.2f}<extra></extra>",
            ))
        fig8.update_layout(
            yaxis_range=[0, 1],
            xaxis_title="Data",
            yaxis_title="Indicador Total",
            hovermode="x unified",
        )
        _add_release_lines(fig8)
        st.plotly_chart(fig8, use_container_width=True)

        st.markdown("---")
