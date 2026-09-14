# Orçamento de Hospedagem — DK Fashion

> **Projeto:** DK Fashion – Marketplace de Moda  
> **Elaborado por:** Equipe de Desenvolvimento DK Fashion  
> **Data:** 24 de Junho de 2026  
> **Cotação utilizada:** US$ 1,00 = R$ 5,20 (câmbio comercial de 24/06/2026)

---

## Resumo Executivo

Este documento apresenta o orçamento detalhado dos custos de hospedagem do site **DK Fashion**, um marketplace de moda composto por:

| Componente | Tecnologia | Descrição |
| :--- | :--- | :--- |
| **Frontend** | React + Vite + TailwindCSS | Interface do usuário (SPA) |
| **Backend (API)** | NestJS + TypeORM | API REST com autenticação JWT |
| **Banco de Dados** | PostgreSQL | Armazenamento relacional de dados |
| **Documentação** | MkDocs (Material) | Portal de documentação técnica |

Atualmente, o projeto está hospedado no **Render.com** utilizando o plano gratuito (Free Tier), que possui limitações críticas para operação comercial. Abaixo, apresentamos **2 cenários de hospedagem paga** para avaliação da cliente.

---

## Situação Atual — Por que sair do Plano Gratuito?

O plano gratuito do Render possui **limitações críticas** que inviabilizam a operação comercial:

| Limitação | Impacto no Negócio |
| :--- | :--- |
| **Cold Start (spin down após 15 min)** | O servidor "adormece" após 15 minutos sem acesso. A primeira requisição pode levar **30–60 segundos** para responder — inaceitável para uma loja online. |
| **Banco de dados expira em 30 dias** | O PostgreSQL gratuito no Render é **temporário** — expira após 30 dias e **todos os dados de produtos, clientes e pedidos são apagados**. |
| **Recursos limitados** | 512 MB RAM, 0.1 CPU — travamentos frequentes com poucos acessos simultâneos. |
| **Sem domínio customizado profissional** | O endereço do site fica como `dkfashion.onrender.com`, sem credibilidade para clientes. |
| **Sem SLA de disponibilidade** | Sem garantia de uptime — o site pode ficar fora do ar sem aviso. |

> **Conclusão:** A migração para um plano pago é **indispensável** para operar comercialmente com segurança e profissionalismo.

---

## Cenários de Hospedagem

---

### Cenário 1 — Básico (Produção Inicial)

**Ideal para:** Lançamento da loja, primeiros clientes, operação com tráfego baixo a moderado (até ~500 visitas/dia).

#### Opção A — Render (Tudo em um lugar)

| Serviço | Plano | Recursos | Custo (USD/mês) | Custo (BRL/mês) |
| :--- | :--- | :--- | ---: | ---: |
| Backend (API) | Render Starter | 512 MB RAM, 0.5 CPU — sem cold starts | $7,00 | R$ 36,40 |
| Banco de Dados | Render PostgreSQL Starter | 1 GB storage, compute básico, persistente | ~$7,00 | R$ 36,40 |
| Frontend | Vercel Hobby | CDN global, HTTPS/SSL, deploy automático | $0,00 | R$ 0,00 |
| Documentação | GitHub Pages | Hospedagem gratuita para docs | $0,00 | R$ 0,00 |
| Workspace | Render Hobby | Gestão do workspace | $0,00 | R$ 0,00 |
| **TOTAL MENSAL** | | | **~$14,00** | **~R$ 72,80** |
| **TOTAL ANUAL** | | | **~$168,00** | **~R$ 873,60** |

#### Opção B — Railway (Melhor custo-benefício)

| Serviço | Plano | Recursos | Custo (USD/mês) | Custo (BRL/mês) |
| :--- | :--- | :--- | ---: | ---: |
| Backend + DB | Railway Hobby | Uso sob demanda (inclui $5 crédito), sem cold starts | ~$8,00 | R$ 41,60 |
| Frontend | Vercel Hobby | CDN global, HTTPS/SSL, deploy automático | $0,00 | R$ 0,00 |
| Documentação | GitHub Pages | Hospedagem gratuita para docs | $0,00 | R$ 0,00 |
| **TOTAL MENSAL** | | | **~$8,00** | **~R$ 41,60** |
| **TOTAL ANUAL** | | | **~$96,00** | **~R$ 499,20** |

> **Por que Railway é recomendado?** A cobrança é por consumo real de recursos (CPU, RAM, storage). Para um backend NestJS + PostgreSQL com tráfego baixo, o custo fica entre $6 e $12/mês — mais econômico que pagar instâncias fixas.
---

### Cenário 2 — Profissional (Produção Completa)

**Ideal para:** Operação comercial consolidada, domínio próprio, alta disponibilidade, crescimento planejado.

#### Opção A — Render Pro

| Serviço | Plano | Recursos | Custo (USD/mês) | Custo (BRL/mês) |
| :--- | :--- | :--- | ---: | ---: |
| Workspace | Render Pro | Autoscaling, previews, 25 GB bandwidth | $25,00 | R$ 130,00 |
| Backend (API) | Render Standard | 2 GB RAM, 1 CPU — alta performance | $25,00 | R$ 130,00 |
| Banco de Dados | Render PostgreSQL Standard | 10 GB storage, compute dedicado | ~$20,00 | R$ 104,00 |
| Frontend | Vercel Pro | 1 TB bandwidth, domínio customizado, analytics | $20,00 | R$ 104,00 |
| Documentação | GitHub Pages | Hospedagem gratuita para docs | $0,00 | R$ 0,00 |
| Domínio `.com.br` | Registro.br | Registro anual do domínio | ~$3,33 | R$ 40,00/ano |
| **TOTAL MENSAL** | | | **~$93,33** | **~R$ 508,00** |
| **TOTAL ANUAL** | | | **~$1.120,00** | **~R$ 6.096,00** |

#### Opção B — Railway Pro 
| Serviço | Plano | Recursos | Custo (USD/mês) | Custo (BRL/mês) |
| :--- | :--- | :--- | ---: | ---: |
| Backend + DB | Railway Pro | Uso sob demanda (inclui $20 crédito), autoscaling | ~$30,00 | R$ 156,00 |
| Frontend | Vercel Pro | 1 TB bandwidth, domínio customizado, analytics | $20,00 | R$ 104,00 |
| Documentação | GitHub Pages | Hospedagem gratuita para docs | $0,00 | R$ 0,00 |
| Domínio `.com.br` | Registro.br | Registro anual do domínio | ~$3,33 | R$ 40,00/ano |
| **TOTAL MENSAL** | | | **~$53,33** | **~R$ 300,00** |
| **TOTAL ANUAL** | | | **~$640,00** | **~R$ 3.600,00** |

---

## Quadro Comparativo Geral

| | 💼 Básico (Render) | 💼 Básico (Railway) | 🚀 Pro (Render) | 🚀 Pro (Railway) |
| :--- | :---: | :---: | :---: | :---: |
| **Custo Mensal (BRL)** | ~R$ 73 | ~R$ 42 | ~R$ 508 | ~R$ 300 |
| **Custo Anual (BRL)** | ~R$ 874 | ~R$ 499 | ~R$ 6.096 | ~R$ 3.600 |
| Performance | ✅ Boa | ✅ Boa | ✅✅ Excelente | ✅✅ Excelente |
| Sem Cold Starts | ✅ Sim | ✅ Sim | ✅ Sim | ✅ Sim |
| Banco Persistente | ✅ Sim | ✅ Sim | ✅ Sim | ✅ Sim |
| Domínio Próprio | ⚠️ Limitado | ⚠️ Limitado | ✅ Total | ✅ Total |
| SSL/HTTPS | ✅ Sim | ✅ Sim | ✅ Sim | ✅ Sim |
| Autoscaling | ❌ Não | ❌ Não | ✅ Sim | ✅ Sim |
| SLA de Uptime | ❌ Não | ❌ Não | ✅ Sim | ✅ Sim |
| Suporte Técnico | ⚠️ Básico | ⚠️ Básico | ✅ Prioritário | ✅ Prioritário |
| Deploy Automático | ✅ Sim | ✅ Sim | ✅ Sim | ✅ Sim |

---

## Recomendação da Equipe

### Para iniciar a operação comercial imediatamente:

> **Cenário 1 — Opção B (Railway Hobby) — ~R$ 42/mês**

**Justificativa:**

- Melhor custo-benefício para início de operação
- Cobrança por consumo real — não paga por recursos ociosos
- Sem cold starts — experiência fluida para o cliente final
- Banco de dados persistente e confiável
- Deploy automático via GitHub
- Fácil upgrade para plano Pro quando o tráfego crescer

### Para operação comercial consolidada (quando o negócio crescer):

> **Cenário 2 — Opção B (Railway Pro + Vercel Pro) — ~R$ 300/mês**

**Justificativa:**

- Performance excelente para centenas de acessos simultâneos
- Domínio próprio profissional (`dkfashion.com.br`)
- Frontend otimizado via CDN global (Vercel)
- Autoscaling — absorve picos de tráfego (ex: promoções, datas comemorativas)
- ecursos escaláveis conforme a demanda

---

## Custos Adicionais Opcionais

Dependendo das necessidades futuras do negócio, podem haver custos extras:

| Item | Estimativa (BRL) | Observação |
| :--- | ---: | :--- |
| Domínio `.com.br` | R$ 40,00/ano | Registro no Registro.br |
| E-mail profissional (Google Workspace) | R$ 37,00/usuário/mês | E-mail @dkfashion.com.br |
| CDN adicional (Cloudflare Pro) | R$ 104,00/mês | Proteção DDoS avançada, WAF |
| Monitoramento (Better Uptime) | R$ 0 – R$ 130,00/mês | Alertas de uptime via SMS/e-mail |
| Backup externo do banco | R$ 0 – R$ 52,00/mês | Backup automatizado em nuvem |
| Certificado SSL customizado | R$ 0,00 | Já incluso em todas as plataformas |

---

## Notas Importantes

1. **Os valores em BRL são estimativas** baseadas na cotação do dólar de 24/06/2026 (US$ 1 = R$ 5,20). A variação cambial pode alterar os valores finais.

2. **Os custos de hospedagem são cobrados em dólar (USD)** diretamente no cartão de crédito internacional. Taxas de IOF (6,38%) e spread bancário podem ser aplicadas pelo banco emissor, o que pode acrescentar aproximadamente **7–10% ao valor final**.

3. **Integrações externas** (InfinitePay para pagamentos, Melhor Envio para frete, ImgBB para imagens) possuem **custos próprios** que não estão incluídos neste orçamento, pois são custos operacionais do negócio.

4. **A migração entre plataformas** (ex: do Render para Railway) pode ser feita sem downtime significativo, já que o projeto utiliza Docker e variáveis de ambiente padronizadas.

5. **Escalabilidade:** Todas as plataformas recomendadas permitem upgrade de plano conforme o crescimento do tráfego, sem necessidade de migração completa.


> *Este orçamento foi elaborado com base nos preços públicos das plataformas em junho de 2026. Os valores podem sofrer alterações sem aviso prévio pelos provedores. Recomendamos verificar os valores atualizados nos sites oficiais antes da contratação.*
