# 📊 Advanced Portfolio Risk & Performance Dashboard – Quantitative Finance Tool

**PhD in Physics | Quantitative Finance Consultant**  
*A professional-grade Python dashboard for portfolio analysis, risk assessment, and stress testing – built for investors, advisors, and financial teams.*

---

## 🎯 **What This Tool Solves**
> Investors and financial managers often rely on **spreadsheets or opaque platforms** to assess portfolio risk. This leads to:
> - **Hidden exposures** to market downturns
> - **Manual, error-prone** calculations of VaR, CVaR, drawdowns
> - **No clear visualization** of stress scenarios
> - **Lack of reproducibility** in analysis

**This dashboard provides:**
✅ **Real‑time risk metrics** (VaR, CVaR, volatility, Sharpe ratio)  
✅ **Interactive stress testing** – simulate market crashes, sector shocks  
✅ **Performance attribution** – understand what drives returns  
✅ **Professional visuals** – ready for client presentations or internal reviews  
✅ **Transparent, auditable code** – no black‑box models

---

## 🏗️ **Architecture & Tech Stack**
```
portfolio_optimizer/
│
├── app/
│ └── dashboard.py # Streamlit frontend
│
├── src/
│ ├── data_loader.py # Loads CSV, API, or Bloomberg-like data
│ ├── metrics.py # Risk & performance calculations
│ ├── optimizer.py # Portfolio optimization (MPT, Black-Litterman)
│ └── plots.py # Interactive Plotly/Matplotlib charts
│
├── data/
│ └── sample_portfolio.csv # Example equity portfolio
│
├── docs/
│ └── Portfolio_Optimizer_Executive_Overview.pdf
│
└── README.md
```

**Technology Stack:**  
![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-green) ![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-orange) ![Plotly](https://img.shields.io/badge/Plotly-Interactive_Visuals-purple) ![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard_App-red)

---

## 📊 **Key Analytical Features**

### 1. **Performance Analytics**
- Cumulative returns vs. benchmarks
- Rolling volatility and Sharpe ratio
- Maximum drawdown analysis

### 2. **Risk Metrics (Production‑Grade)**
- **Value at Risk (VaR)** – Historical, parametric, Monte Carlo
- **Conditional VaR (CVaR)** – Expected loss in worst‑case scenarios
- **Portfolio beta & correlation heatmaps**
- **Sector/concentration risk** exposure

### 3. **Stress Testing & Scenarios**
- **Custom shock scenarios** (e.g., -20% tech sector, +5% rates)
- **Historical crisis replay** (2008, 2020 COVID, etc.)
- **Monte Carlo simulations** for forward‑looking risk

### 4. **Optimization Module**
- **Modern Portfolio Theory (MPT)** – Efficient frontier
- **Risk‑parity allocation**
- **Black‑Litterman** for incorporating market views

---

## 🚀 **Quick Start – Run in 3 Minutes**

### 1. **Clone & Setup**
```bash
git clone https://github.com/hgrubina/portfolio_optimizer.git
cd portfolio_optimizer
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Launch Dashboard
```bash

streamlit run app/dashboard.py
```
Open browser: http://localhost:8501

### 3. Upload Your Data

    Use provided sample_portfolio.csv as template

    Replace with your own holdings (CSV: ticker,shares,entry_date)

    Adjust parameters (confidence level, time horizon) in sidebar

📸 Dashboard Preview


👥 Who Is This For?
|                         |                                                             |
|-------------------------|-------------------------------------------------------------|
| User                    | Use Case                                                    |
| Individual Investors    | Understand risk exposure beyond basic broker reports        |
| Financial Advisors      | Client presentations with professional, interactive visuals |
| Portfolio Managers      | Quick stress‑testing of allocations before rebalancing      |
| Quantitative Analysts   | Extensible codebase for custom risk models                  |
| Wealth Management Firms | Internal tool for consistent risk reporting                 |

🔮 Ready‑to‑Implement Extensions

    ✅ API integrations – Yahoo Finance, Alpha Vantage, Bloomberg

    ✅ Multi‑asset support – equities, bonds, crypto, real estate

    ✅ Automated reporting – PDF generation, email alerts

    ✅ Cloud deployment – AWS/GCP, Docker containerization

    ✅ Machine‑learning enhancements – LSTM VaR, regime‑switching models

📄 Executive Documentation

A complete business‑oriented overview is available:
➡️ Portfolio Optimizer – Executive Overview (PDF)

Includes:

    Methodology behind each risk metric

    Regulatory considerations (Basel, MiFID)

    Integration pathways with existing systems

    Case study: Portfolio stress during 2020 crash

👨‍💻 About the Author

Hernán Grubina – PhD in Physics | Quantitative Finance & Risk Consultant
I apply scientific rigor and advanced modeling to investment and risk problems – turning complex mathematics into actionable, auditable tools.

📫 Let’s optimize your portfolio with science, not guesswork:
PeoplePerHour Profile
GitHub Profile: hgrubina
mail: hgrubina.dev@gmail.com

⚠️ Disclaimer

This tool is for professional financial analysis and education. It does not constitute investment advice. Past performance is not indicative of future results. Always consult a qualified financial advisor before making investment decisions.
