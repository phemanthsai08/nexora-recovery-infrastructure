# ⚡ Nexora — Intelligent Revenue Recovery Infrastructure

> **Autonomous AI agent that recovers failed payments with culturally-native Hinglish outreach, structured Promise-to-Pay extraction, Razorpay settlement, and strict ethical guardrails.**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![Anthropic Claude](https://img.shields.io/badge/Claude-Sonnet-black?logo=anthropic)](https://anthropic.com)
[![Razorpay](https://img.shields.io/badge/Razorpay-Testnet-3395FF?logo=razorpay)](https://razorpay.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

### Why this exists

In high-growth Indian digital businesses, **15–30% of GMV** is routinely lost to failed cards, UPI timeouts, low balances, and abandoned checkouts. Most recovery systems either:

- Spam customers with aggressive templates → destroy LTV
- Or do almost nothing → leave money on the table

**Nexora** sits in the middle: an agentic system that speaks natural Hinglish, extracts real promises, creates live Razorpay payment links, and is hard-bounded by deterministic policy rules so it never harasses.

This is a complete, runnable demonstration of **production-grade agentic fintech** — not a toy chatbot.

---

## ✨ What you get out of the box

| Capability | Detail |
| :--- | :--- |
| **Empathetic Hinglish Engine** | Context-aware messages in Hinglish / Hindi / English tailored to failure reason (card limit, liquidity, UPI, etc.) |
| **Structured Promise-to-Pay** | Turns free-text customer replies into date + confidence + intent + sentiment |
| **Live Razorpay Testnet** | Real payment links + order retry simulation |
| **8 Deterministic Rules (R1–R8)** | Hard caps on retries, high-value human review gate (₹50k), cooldown, Ghost Protocol graceful halt |
| **Immutable Audit Trail** | Every decision is logged with reasoning — ready for compliance review |
| **Mission Control Dashboard** | Beautiful enterprise fintech UI with live metrics, record explorer, CoT sandbox, theme switcher |
| **Full 55-record batch** | Realistic synthetic cohort with measured recovery metrics |

---

## 🏗️ Architecture (one glance)

```
Payment Failure
      │
      ▼
┌─────────────────────────┐
│ 1. Rule Engine (R1–R8)  │  ← deterministic policy gates
└───────────┬─────────────┘
            │
     ┌──────┴──────┐
     │             │
  BLOCKED       PASSED
     │             │
     ▼             ▼
 Clean Halt /   Empathetic Message Generator (Claude)
 Human Review         │
                      ▼
               Reply Simulation / Real Reply
                      │
                      ▼
               Promise Extractor (structured)
                      │
                      ▼
               Razorpay Settlement + Deadline Tracker
                      │
                      ▼
               Immutable Audit + Metrics
```

---

## 🚀 Quick Start (local)

```bash
# 1. Clone
git clone https://github.com/phemanthsai08/nexora-recovery-infrastructure.git
cd nexora-recovery-infrastructure

# 2. Install
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Configure (optional for full AI + Razorpay)
cp .env.example .env
# Edit .env and add:
# ANTHROPIC_API_KEY=sk-ant-...
# RAZORPAY_KEY_ID=rzp_test_...
# RAZORPAY_KEY_SECRET=...

# 4. Launch
python backend/server.py
```

Open → **http://localhost:8000**

You can immediately explore the dashboard, metrics, audit log, and run the sandbox simulator even without API keys (mock mode). With keys you get real Claude messages + live Razorpay links.

---

## 🖥️ Dashboard Highlights

- **Mission Control** — live recovery metrics, capital at stake, promise keep rate
- **Record Explorer** — searchable 55-record cohort with filters
- **Sandbox Simulator** — type a customer reply and watch full Chain-of-Thought + promise extraction
- **Audit Trail** — every rule decision, message, and action with reasoning
- **Ghost Protocol** — deliberate graceful failure demonstration
- **Theme Switcher** — Slate / Emerald / Violet enterprise accents
- **One-click Pipeline** — run the full batch from the UI

---

## 📊 Batch Results (55 synthetic records)

| Metric | Value |
| :--- | ---: |
| Total Capital at Stake | ₹5,33,260 |
| Capital Recovered | ₹82,485 (**15.5%** of total / **27.3%** of recoverable) |
| Promises Extracted | 32 (58.2%) |
| Promise Keep Rate | 46.9% |
| Clean Policy Halts | 3 |
| Human Review Escalations | 9 |

These numbers come from an unbiased full-cohort run, not cherry-picked examples.

---

## 🛡️ Policy Guardrails (R1–R8)

The agent is deliberately **not** fully autonomous. Hard rules include:

- High-value gate (₹10k+) requires explicit logging
- Human review mandatory above ₹50,000
- Max 2 outreach attempts
- 24-hour cooldown between messages to the same customer
- Max 2 broken promises → permanent stop (Ghost Protocol)
- No messaging on disputes / legal flags
- Clean halt on certain failure types

This is intentional: real fintech agents must be bounded.

---

## 📁 Project Structure

```
nexora-recovery-infrastructure/
├── backend/
│   └── server.py              # FastAPI app + static frontend
├── agent/
│   ├── config.py              # Keys, thresholds, paths
│   ├── rule_engine.py         # R1–R8 deterministic gates
│   ├── message_generator.py   # Claude Hinglish outreach
│   ├── promise_extractor.py   # Structured PTP extraction
│   ├── razorpay_client.py     # Payment links & settlement
│   ├── promise_tracker.py     # Deadline radar
│   ├── reply_simulator.py     # Synthetic customer replies
│   ├── storage.py             # Metrics + audit helpers
│   ├── run_pipeline.py        # Full batch runner
│   └── run_step2.py
├── frontend/                  # Pure HTML/CSS/JS dashboard
│   ├── index.html
│   ├── app.js
│   └── style.css
├── data/                      # Synthetic + processed records
├── logs/                      # Audit, metrics, promises
├── .env.example
└── requirements.txt
```

---

## 🔑 Environment Variables

```env
ANTHROPIC_API_KEY=sk-ant-api03-...
RAZORPAY_KEY_ID=rzp_test_...
RAZORPAY_KEY_SECRET=...
```

Without keys the system still runs in demo/mock mode so the UI and pipeline remain fully explorable.

---

## 🌐 Deploy Notes

### Local (recommended for full experience)
```bash
python backend/server.py
```

### Cloud options
This is a classic FastAPI + static frontend app. Best experiences:

- **Railway / Render / Fly.io** — one-click Python deploy (recommended for the full dashboard + API)
- **Vercel** — great for the static frontend; API routes can be adapted to serverless or you can proxy to a separate backend

A production-ready container or platform deploy will give the richest demo.

---

## 🎯 Who this is for

- **Builders** who want a reference architecture for agentic fintech
- **Hiring managers** looking for evidence of real agent design (not just prompt engineering)
- **Founders** exploring intelligent collections without destroying brand trust
- **Students / researchers** studying constrained autonomous agents + cultural NLP (Hinglish)

---

## 📜 License

MIT — use it, fork it, build on it. Attribution appreciated.

---

**Built as a complete, production-minded demonstration of bounded autonomous agents in the Indian fintech context.**

If you find this useful, star the repo and open an issue with ideas or improvements.
