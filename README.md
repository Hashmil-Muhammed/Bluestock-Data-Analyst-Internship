<div align="center">

# 📊 Bluestock Fintech Data Analyst Internship Portfolio

---

### 🚀 From Learning Fundamentals to Building an End-to-End Mutual Fund & Nifty 100 Analytics Platform

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-green?style=for-the-badge&logo=sqlite&logoColor=white)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow?style=for-the-badge&logo=powerbi&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-Analytics-purple?style=for-the-badge&logo=pandas&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black?style=for-the-badge&logo=github&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Internship-Ongoing-blue?style=for-the-badge&logo=checkmarx&logoColor=white)

</div>

---

## 📋 Table of Contents

- [🎯 Internship Overview](#-internship-overview)
- [🚀 Week 1: Intensive Learning Phase](#-week-1-intensive-learning-phase)
- [📊 Project 1: Mutual Fund Analytics Platform](#-project-1-mutual-fund-analytics-platform)
- [📈 Project 2: Nifty 100 Financial Intelligence Platform](#-project-2-nifty-100-financial-intelligence-platform)
- [🏆 Internship Achievements](#-internship-achievements)
- [🛠️ Technology Stack](#️-technology-stack)
- [🏗️ Repository Structure](#️-repository-structure)
- [📸 Learning Journey](#-learning-journey)
- [🚀 How to Run the Projects](#-how-to-run-the-projects)
- [📬 Contact](#-contact)

---

## 🎯 Internship Overview

This repository showcases my complete journey during the **Bluestock Fintech Data Analyst Internship**.

Over the course of this intensive internship, I progressed from foundational Python programming and database concepts to developing two major production-ready projects: a **Mutual Fund Analytics Platform** and an end-to-end **Nifty 100 Financial Intelligence Platform**.

### Key Focus Areas

- Python Programming & Pytest
- Data Analysis & Visualization
- SQL & Database Engineering (SQLite & PostgreSQL)
- Financial Analytics & Algorithmic Engines
- API Integration (FastAPI)
- ETL Pipeline Development
- Power BI Dashboard Development
- Machine Learning Fundamentals
- End-to-End Data Engineering

---

## 🚀 Week 1: Intensive Learning Phase
*Foundational training in data analytics, database management, and fintech concepts.*

| Day | Milestone |
| :--- | :--- |
| **Day 1** | Python Fundamentals & Environment Setup |
| **Day 2** | Data Manipulation (NumPy, Pandas, EDA) |
| **Day 3** | SQL & Database Engineering (Joins, CTEs, PostgreSQL) |
| **Day 4** | Data Visualization & REST API Integration |
| **Day 5** | Fintech Fundamentals (NAV, CAGR, SIP) & ML Basics |

---

## 📊 Project 1: Mutual Fund Analytics Platform
*The core phase focused on developing, automating, and deploying the initial Capstone Project.*

| Day | Milestone |
| :--- | :--- |
| **Day 6-7** | Data Ingestion, SQL Star Schema Design & ETL Pipeline |
| **Day 8-9** | Exploratory Data Analysis (EDA) & Performance Analytics |
| **Day 10** | Power BI Interactive Dashboard Development |
| **Day 11** | Advanced Risk Metrics (VaR, CVaR, HHI) |
| **Day 12** | Robo-Advisor Recommender System Development |
| **Day 13** | Pipeline Automation & Final Documentation |
| **Bonus** | **Enterprise Automation (Scheduler, Email Reports, Monte Carlo & Optimization)** |
| **Bonus** | **Cloud Deployment (Streamlit Web Application)** |

### 📈 Mutual Fund Project Highlights
* **Data Engineering:** ETL pipeline with SQLAlchemy, SQLite Star Schema design.
* **Financial Analytics:** Alpha/Beta, Sharpe/Sortino Ratios, Maximum Drawdown calculation.
* **Predictive Modeling:** Monte Carlo Simulation (5-Year NAV Projections).
* **Portfolio Optimization:** Markowitz Efficient Frontier (Optimal Asset Allocation).
* **Automation:** Weekly Email Reporting & Automated Watchdog Scheduler.
* **Business Intelligence:** Interactive Power BI Dashboards & Live Streamlit Web Application.

---

## 📈 Project 2: Nifty 100 Financial Intelligence Platform
*An advanced, end-to-end platform analyzing data for the Nifty 100 companies. The project processes 12 source datasets across 12 distinct modules over a 45-day execution plan.*

**Status:** `Sprint 1 - Completed`

### 📅 Sprint 1 Progress: Data Foundation (Day 1 to Day 7)

* **Day 01: Environment & Project Foundation:** Established a professional workspace layout (`src/`, `tests/`, `data/`, `reports/`). Set up a clean virtual environment, configured `requirements.txt`, created a custom `Makefile`, and a Windows `.bat` script for quick activation.
* **Day 02: Data Loader & Normalizer Engine:** Developed robust data cleansing functions (`normalize_ticker`, `normalize_year`) in `src/etl/normaliser.py`. Built an automated pipeline (`loader.py`) to read complex Excel files. Authored 23 rigorous unit tests with 100% passing results via Pytest-HTML.
* **Day 03: Schema Validator (16 DQ Rules):** Developed `validator.py` to ensure data integrity. Coded critical checks including PK/FK uniqueness, Balance Sheet tally verification, and Positive Sales validation.
* **Day 04: Database Schema Engineering:** Architected the foundational SQLite Star Schema (`schema.sql`). Written strict DDL statements for 12 core tables enforcing Foreign Key constraints.
* **Day 05: Database Loader Pipeline:** Integrated the loader to automatically ingest all 12 validated Excel datasets into a centralized `nifty100.db` SQLite database, generating a `load_audit.csv` report.
* **Day 06: Data Quality Manual Review:** Performed manual checks via direct SQL queries using a temporary script to verify table structures and check year coverage (e.g., identifying newly listed companies like `JIOFIN` having `< 5 years` of data).
* **Day 07: Sprint Wrap-Up:** Executed 10 exploratory SQL queries directly on `nifty100.db` to verify data completeness. Expanded Pytest unit test coverage to 38 tests (100% pass rate) across ETL components.

---

## 🏆 Internship Achievements

- ✅ Completed Bluestock Fintech Data Analyst Internship
- ✅ Developed End-to-End Mutual Fund Analytics Platform
- ✅ Built Interactive Power BI Dashboard
- ✅ Designed Star Schema Data Warehouse
- ✅ Implemented SQLAlchemy & Pandas ETL Pipelines
- ✅ Developed Risk-Based Fund Recommendation System
- ✅ Executed Comprehensive Pytest Testing Suites
- ✅ Automated Complete Data Processing Workflows

---

## 🛠️ Technology Stack

| Category | Technologies |
|-----------|-------------|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Dashboarding | Power BI |
| Database | PostgreSQL, SQLite |
| Testing & QA | Pytest, Pytest-HTML |
| APIs | FastAPI, Flask, REST APIs |
| Tools | Git, GitHub, Jupyter Notebook, Streamlit Cloud |

---

## 🏗️ Repository Structure

```text
📦 Bluestock-Data-Analyst-Internship
 ┣ 📂 Hashmil_Submission                             # Internship Submission Assets
 ┣ 📂 bluestock_mf_capstone                          # Project 1: Mutual Fund Analytics
 ┃ ┣ 📂 data                                         # Raw, Processed & SQLite DB
 ┃ ┣ 📂 notebooks                                    # Sequential Analysis Workspaces
 ┃ ┣ 📂 scripts                                      # Automation & Predictive Engines
 ┃ ┣ 📂 reports                                      # Analytics Exports & Visuals
 ┃ ┗ 📜 run_pipeline.py                              # Pipeline Controller
 ┣ 📂 N100 FINANCIAL INTELLIGENCE PLATFORM           # Project 2: Nifty 100 Platform
 ┃ ┣ 📂 data                                         # Raw and supporting Excel files
 ┃ ┣ 📂 src                                          # ETL, analytics, dashboard, api
 ┃ ┣ 📂 tests                                        # Pytest suite (38+ tests)
 ┃ ┣ 📂 reports                                      # Pytest HTML & Audit CSVs
 ┃ ┣ 📜 nifty100.db                                  # Primary SQLite database
 ┃ ┣ 📜 Makefile                                     # Automation targets
 ┃ ┗ 📜 activate_env.bat                             # Env activation
 ┣ 📂 learning-journey-week1                         # Week 1 Skill Progress Images
 ┣ 📂 Capstone-Project_journey-week2                 # capstone Milestone Snapshots
 ┣ 📂 N100_financial_intelligence-Project_journey    # N100 Milestone Snapshots
 ┗ 📜 README.md

```

## 🚀 How to Run the Project

### Clone Repository

```bash
git clone https://github.com/Hashmil-Muhammed/Bluestock-Data-Analyst-Internship.git

cd bluestock-data-analyst-internship
```
<!-- 
### Install Dependencies

```bash
pip install -r requirements.txt
``` -->

### 🔹 Project 1: Mutual Fund Pipeline

```bash
# Run Live NAV Fetcher
python bluestock_mf_capstone/scripts/live_nav_fetch.py

# Run Fund Recommendation Engine
python bluestock_mf_capstone/scripts/recommender.py

# Run Complete Pipeline
python bluestock_mf_capstone/run_pipeline.py
```

### 🔹 Project 2: Nifty 100 ETL Pipeline (Sprint 1)

```bash
cd "N100 FINANCIAL INTELLIGENCE PLATFORM"
.\activate_env.bat

# Run the database loader pipeline
make load

# Execute unit tests & generate HTML report
make test
```

---

### 🌐 Access the Web App
Visit the [Bluestock Analytics Pro](https://bluestock-analytics-hashmil.streamlit.app/) to explore the interactive dashboard.

---

## 📬 Contact

### Hashmil Muhammed

📧 Email: hashmilmuhammedparammal@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/hashmil-muhammed08/

🔗 GitHub: https://github.com/Hashmil-Muhammed

---

<div align="center">

## ⭐ Internship Completed Successfully ⭐

### From Python Fundamentals ➜ Data Analytics ➜ Financial Engineering ➜ Power BI ➜ End-to-End Mutual Fund Analytics Platform

Thank you for visiting my Bluestock Internship Portfolio.

</div>