<div align="center">

# 📈 Nifty 100 Financial Intelligence Platform
### End-to-End Financial Analytics & Business Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-green?style=for-the-badge&logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Analytics-purple?style=for-the-badge&logo=pandas&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black?style=for-the-badge&logo=github&logoColor=white)


<br>

---
</div>

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [📅 Sprint 1 Progress Tracker (Data Foundation)](#-sprint-1-progress-tracker-data-foundation)
- [📅 Sprint 2 Progress Tracker (Analytics Engine)](#-sprint-2-progress-tracker-analytics-engine)
- [📅 Sprint 3 Progress Tracker (Screener & Ranking Engine)](#-sprint-3-progress-tracker-screener--ranking-engine)
- [📅 Sprint 4 Progress Tracker (Dashboard & Valuation)](#-sprint-4-progress-tracker-dashboard--valuation)
- [📂 Repository Structure](#-repository-structure)
- [🛠️ Execution & Setup Guide](#️-execution--setup-guide)

---

## 🎯 Project Overview

This repository contains the Capstone Project for the **Bluestock Fintech Data Analytics Internship**.

The goal of this project is to build an end-to-end Financial Intelligence Platform analyzing data for the Nifty 100 companies. The project processes 12 source datasets (7 core and 5 supplementary) across 12 distinct modules over a 45-day execution plan.

**Sprints Completed:** `Sprint 1`, `Sprint 2`, `Sprint 3`

**Status:** `Sprint 4 (Dashboard Development) - In Progress`
---

## 📅 Sprint 1 Progress Tracker (Data Foundation)

### 🔹 Day 01: Environment & Project Foundation
- **Directory Structure:** Established a professional workspace layout (`src/`, `tests/`, `data/`, `reports/`).
- **Virtual Environment:** Set up a clean Python virtual environment (`.venv`) to isolate dependencies.
- **Dependency Management:** Configured `requirements.txt` with core data science and analytical libraries.
- **Environment Variables:** Set up `.env` for managing sensitive configurations like database paths and ports.
- **Automation:** Created a custom `Makefile` and a Windows batch script (`activate_env.bat`).

### 🔹 Day 02: Data Loader & Normalizer Engine
- **Normalizer Logic (`src/etl/normaliser.py`):** Developed robust data cleansing functions for tickers and financial years.
- **Data Loading Pipeline (`src/etl/loader.py`):** Programmed an automated pipeline using `pandas` to read Excel files.
- **Unit Test Suite (`tests/etl/test_normalise.py`):** Authored 23 rigorous unit tests evaluating edge cases.

### 🔹 Day 03: Schema Validator (16 DQ Rules)
- **Data Quality Engine (`src/etl/validator.py`):** Developed a robust data validation class.
- **Rule Implementation:** Coded checks including PK/FK uniqueness and Balance Sheet tally verification.

### 🔹 Day 04: Database Schema Engineering
- **Schema Design (`src/etl/schema.sql`):** Architected the foundational SQLite Star Schema layout.
- **Table Creation:** Written strict DDL statements for 12 tables.

### 🚀 Day 05: Database Loader Pipeline
- **Objective:** Ingest all 12 validated Excel datasets into a centralized SQLite database.
- **Actions:** Loaded data into all tables and generated a load audit report (`reports/load_audit.csv`).

### 🧐 Day 06: Data Quality Manual Review
- **Objective:** Perform manual checks on the loaded SQLite database.
- **Actions:** Queried random companies and checked for minimum year coverage (e.g., `JIOFIN`).

### 🏁 Day 07: Sprint Wrap-Up
- **Objective:** Ensure pipeline stability and finalize Sprint 1.
- **Actions:** Executed exploratory SQL queries and achieved 100% pass rate across 38 unit tests.

---

## 📅 Sprint 2 Progress Tracker (Analytics Engine)

### 📈 Day 08: Profitability Ratios Implementation
- **Objective:** Program core profitability ratios.
- **KPIs Computed:** Net Profit Margin (NPM), Operating Profit Margin (OPM), Return on Equity (ROE), and Return on Capital Employed (ROCE).
- **Edge Case Handling:** Handled negative equity and zero sales scenarios.

### ⚖️ Day 09: Leverage & Efficiency Ratios
- **Objective:** Build metrics to evaluate corporate debt levels and asset utilization.
- **KPIs Computed:** Debt-to-Equity (D/E) Ratio, Interest Coverage Ratio (ICR), and Asset Turnover Ratio.
- **Edge Case Handling:** Developed Bank Carve-out logic and Debt-free substitution.

### 📊 Day 10: CAGR Calculation Engine
- **Objective:** Engineer a Compound Annual Growth Rate (CAGR) calculator.
- **KPIs Computed:** Revenue CAGR, PAT CAGR, and EPS CAGR (3Y, 5Y, and 10Y).
- **Edge Case Handling:** Integrated "Turnaround Flag Logic" and bypassed negative base complex math.

### 💸 Day 11: Cash Flow KPIs & Allocation Patterns
- **Objective:** Analyze cash flow statements.
- **KPIs Computed:** Free Cash Flow (FCF), CFO Quality Score, CapEx Intensity.
- **Pattern Classification:** Developed a proprietary algorithm to classify companies into 8 Capital Allocation Patterns (e.g., Mature/Cash Cow).

### 🗄️ Day 12: Database Population & Core Ingestion
- **Objective:** Aggregate all calculated analytics and ingest them into SQLite.
- **Actions:** Merged outputs using composite keys (`company_id`, `year`) and uploaded 1,467 processed rows to the `financial_ratios` table.

### 🏦 Day 13: Specialized Banking ROCE Adjustments
- **Objective:** Develop a sector-relative approach for Banks and NBFCs.
- **Actions:** Identified that standard ROCE logic fails for financials (as debt is raw material). Logged 54 anomalies dynamically by comparing calculated values against source benchmarks.
- **Deliverable:** `src/analytics/banking_roce.py` & `reports/sector_roce_notes.csv`

### ✅ Day 14: Final Test Validation & Retrospective
- **Objective:** Ensure mathematical perfection across all programmed KPI formulas.
- **Actions:** Authored 25 edge-case unit tests. Achieved a 100% green pass rate (0 failures). Documented all mathematical workarounds in an edge case log.
- **Deliverable:** `tests/kpi/test_analytics_engine.py`, `reports/ratio_edge_cases.log`, `docs/sprint2_retro.md`

---

## 📅 Sprint 3 Progress Tracker (Screener Engine)

### ⚙️ Day 15: Custom Filter Engine & YAML Configuration
- **Objective:** Build a multi-criteria stock screener engine driven by YAML.
- **Actions:** Configured `screener_config.yaml` and implemented dynamic filtering using Pandas.

### 🔍 Day 16: Preset Screener Implementation
- **Objective:** Configure 6 preset screeners (Quality, Value, Growth, Dividend, Momentum, Debt-free).
- **Actions:** Tested presets on the 92-company universe and verified business logic consistency.

### 🏆 Day 17: Composite Ranking Engine
- **Objective:** Develop a ranking engine using a weighted composite score.
- **Actions:** - Implemented weighting: Profitability (50%), Growth (30%), Valuation (20%).
  - Performed sector-relative normalization.
  - Exported final rankings to `screener_output.xlsx`.

### 🏦 Day 18: Peer Group Module
- **Objective:** Compute peer-relative performance.
- **Actions:** Loaded `peer_groups.xlsx`, calculated `PERCENT_RANK` for key metrics per sector, and populated the `peer_percentiles` table in `nifty100.db`.

### 🕸️ Day 19: Radar Chart Visualization
- **Objective:** Generate visual performance comparisons.
- **Actions:** Engineered a Plotly visualization module to generate radar charts for each company against its peer group median. Exported 56 PNG charts to `reports/radar_charts/`.

### 📊 Day 20: Peer Comparison Excel Reports
- **Objective:** Generate robust, sector-wise peer comparison Excel reports.
- **Actions:** Built `src/reports/peer_comparison.py`. Resolved complex data mapping issues by implementing a Pandas `merge` to accurately join percentile rank data (`peer_percentiles`) with actual financial metrics (`financial_ratios`), ensuring correct ROE and NPM values in the final outputs.

### 🏁 Day 21: Sprint 3 Final Wrap & DQ Tests
- **Objective:** Validate Sprint 3 data integrity and conduct retrospective.
- **Actions:** - Authored and ran `tests/dq/test_dq_sprint3.py`, ensuring all percentile ranks fall strictly within the valid 0-100 bounds and checking for null assignment failures.
  - Achieved 100% Green DQ pass rate.
  - Documented action items, learnings, and data merging workarounds in `docs/sprint3_retro.md`. Sprint 3 officially closed.

---

## 📅 Sprint 4 Progress Tracker (Dashboard & Valuation)

### 📅 Day 22: Dashboard Foundation & Scaffold
- **Task 1:** Established directory structure (`src/dashboard/pages/`).
- **Task 2:** Created `src/dashboard/utils/db.py` with `@st.cache_data` for efficient data fetching.
- **Task 3:** Built `app.py` entry point with custom styling, sidebar logo, and branding.

### 📅 Day 23: Home & Company Profile Screens
- **5.1 Home / Overview:** Displayed market health, top KPIs, and sector donut chart.
- **5.2 Company Profile:** Implemented ticker search, 6-metric KPI tiles, and dynamic charts.

### 📅 Day 24: Screener & Peer Comparison Screens
- **5.3 Financial Screener:** Integrated sidebar sliders for real-time data filtering.
- **5.4 Peer Comparison:** Peer group dropdown selector with integrated Radar Chart visualizations.

### 📅 Day 25: Trend Analysis, Sector & Allocation
- **5.5-5.8 Analysis:** Built Trend sparklines, Sector bubble charts, Capital Allocation Treemap, and Annual Report links.

### 📅 Day 26: Valuation & Market Data Module
- **Valuation Analytics:** Computed P/E, P/B, EV/EBITDA trends using `market_cap.xlsx`. Implemented logic to flag Caution/Discount badges.

### 📅 Day 27: Integration Testing & QA
- **Dashboard QA:** Tested all 8 screens, fixed responsiveness, and documented results in `tests/dq/dashboard_qa.md`.

### 📅 Day 28: Sprint Wrap-Up
- **Retrospective:** Finalized project demo preparation, updated navigation guide, and closed Sprint 4.

---

## 📂 Repository Structure

```text
📦N100 FINANCIAL INTELLIGENCE PLATFORM
 ┣ 📂data
 ┃ ┣ 📂raw                         # 7 core Excel files (READ ONLY).
 ┃ ┗ 📂supporting                  # 5 supplementary Excel files.
 ┣ 📜nifty100.db                   # Primary SQLite database.
 ┣ 📂config
 ┃ ┣ 📜screener_config.yaml        # Screener thresholds configuration
 ┃ ┗ 📜logging_config.yaml       
 ┣ 📂src
 ┃ ┣ 📂etl                         # Extraction, Transformation, and Loading
 ┃ ┃ ┣ 📜exploratory_queries.sql   
 ┃ ┃ ┣ 📜normaliser.py             
 ┃ ┃ ┣ 📜loader.py                 
 ┃ ┃ ┣ 📜validator.py              
 ┃ ┃ ┗ 📜schema.sql                
 ┃ ┣ 📂analytics                   # Ratios, CAGR, Cashflow engines
 ┃ ┃ ┣ 📂screener                  # Multi-criteria Screener Engine
 ┃ ┃ ┃ ┗ 📜engine.py               
 ┃ ┃ ┣ 📜ratios.py                 
 ┃ ┃ ┣ 📜cagr.py                   
 ┃ ┃ ┣ 📜cashflow_kpis.py          
 ┃ ┃ ┣ 📜populate_ratios.py        
 ┃ ┃ ┣ 📜peer.py                   # Peer ranking calculations
 ┃ ┃ ┗ 📜banking_roce.py           # Specialized financial sector analysis
 ┃ ┣ 📂reports                     # Report Generation Scripts
 ┃ ┃ ┣ 📜radar_charts.py           # Radar chart plot generation
 ┃ ┃ ┗ 📜peer_comparison.py        # Sector-wise Excel report builder
 ┃ ┣ 📂nlp                         # Upcoming (Sprint 4)
 ┃ ┣ 📂dashboard                   # Upcoming (Sprint 5)
 ┃ ┗ 📂api                         # Upcoming (Sprint 6)
 ┣ 📂tests                         # Pytest and DQ test files
 ┃ ┣ 📂etl
 ┃ ┃ ┣ 📜test_normalise.py         
 ┃ ┃ ┗ 📜test_validator.py         
 ┃ ┣ 📂kpi
 ┃ ┃ ┣ 📜test_leverage.py          
 ┃ ┃ ┗ 📜test_analytics_engine.py  # 25 full analytics KPI tests
 ┃ ┗ 📂dq
 ┃   ┗ 📜test_dq_sprint3.py        # Sprint 3 Data Quality validation rules
 ┣ 📂reports                       # Exported findings and logs
 ┃ ┣ 📜pytest_report.html          
 ┃ ┣ 📜load_audit.csv              
 ┃ ┣ 📜validation_failures.csv     
 ┃ ┣ 📜sector_roce_notes.csv       # Day 13 Anomaly logs
 ┃ ┗ 📜ratio_edge_cases.log        # Day 14 KPI constraints 
 ┣ 📂output                        
 ┃ ┗ 📜peer_comparison.xlsx        # Generated peer comparison output
 ┣ 📂scripts
 ┃ ┣ 📜ranking_engine.py
 ┃ ┣ 📜check_db.py
 ┃ ┗ 📜screener_preset_test.py
 ┣ 📂notebooks                     
 ┣ 📂docs                          # Analyst guides & Retrospectives
 ┃ ┣ 📜sprint2_retro.md            # Sprint 2 post-mortem analysis
 ┃ ┗ 📜sprint3_retro.md            # Sprint 3 post-mortem analysis
 ┣ 📜.env                          
 ┣ 📜Makefile                      
 ┣ 📜requirements.txt              
 ┗ 📜activate_env.bat
 ```

---

## 🛠️ Execution & Setup Guide

### 1. System Deployment & Virtual Environment Setup

Activate the Python dependency environment:

```powershell
.\activate_env.bat
```

### 2. Execute Unit Tests & Generate Report

Run the comprehensive unit test suite to validate the normalization logic:

```bash
make test
```

### 3. Verify the HTML Test Report

Open the generated file at `reports/pytest_report.html` in any web browser to see the professional pipeline audit execution results.

### 4. Run the Analytics Engine (Profitability Ratios)

Execute the scripts to calculate Ratios and CAGR metrics:

```bash
python -m src.analytics.ratios
python -m src.analytics.cagr
```

### 5. Run the Analytics Engines & Populate Database (Sprint 2)

Execute the master population script to run all analytical modules and ingest data into SQLite:

```bash
python -m src.analytics.populate_ratios
```

### 6. Execute Specialized Banking Analysis

Run the sector-relative ROCE adjustments:

```bash
python -m src.analytics.banking_roce
```

### 7. Execute Complete Unit Test Suite

Run the comprehensive test suite to validate all ETL and Analytics (KPI) logic:

```bash
make test
# OR
pytest tests/
```

### 8. Run the Screener Engine 

Execute the dynamic screener engine to filter companies based on custom parameters:

```bash
python -m src.analytics.screener.engine
```

### 9. Run Screener Engine

```bash
python scripts/screener_preset_test.py
```

### 10. Generate Ranking Report

```bash
python scripts/ranking_engine.py
```

### 11. Generate Peer Percentiles & Charts

```bash
python -m src.analytics.peer
python -m src.reports.radar_charts
```

### 12. Generate Peer Comparison Excel Reports

```bash
python src/reports/peer_comparison.py  
```

### 13. Run Sprint 3 Data Quality (DQ) Tests

```bash
python tests/dq/test_dq_sprint3.py
```
---

## 🚀 How to Run the Dashboard
This project features a fully interactive 9-screen multi-page Streamlit application. Follow these steps to run the dashboard locally:
#### 1. Install Dependencies:
Ensure you have Python installed. Activate your virtual environment and install the required libraries:
```bash
pip install streamlit pandas plotly sqlite3
```

#### 2. Run the Application:
Navigate to the root directory of the project and execute the following command:
```bash
streamlit run src/dashboard/app.py
```

#### 3. Access the Dashboard:
Once the server starts, open your browser and navigate to the local URL provided in the terminal (usually http://localhost:8501).





