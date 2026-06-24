<div align="center">

# 📈 Nifty 100 Financial Intelligence Platform
### End-to-End Financial Analytics & Business Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-green?style=for-the-badge&logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Analytics-purple?style=for-the-badge&logo=pandas&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Sprint_2-In_Progress-yellow?style=for-the-badge)

<br>

---
</div>

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [📅 Sprint 1 Progress Tracker (Data Foundation)](#-sprint-1-progress-tracker-data-foundation)
  - [🚀 Day 1: Environment & Project Foundation](#-day-1-environment--project-foundation)
  - [🛠️ Day 2: Data Loader & Normalizer Engine](#️-day-2-data-loader--normalizer-engine)
  - [🔍 Day 3: Schema Validator (16 DQ Rules)](#-day-3-schema-validator-16-dq-rules)
  - [🗄️ Day 4: Database Schema Engineering](#️-day-4-database-schema-engineering)
  - [🚀 Day 5: Database Loader Pipeline](#-day-5-database-loader-pipeline)
  - [🧐 Day 6: Data Quality Manual Review](#-day-6-data-quality-manual-review)
  - [🏁 Day 7: Sprint Wrap-Up](#-day-7-sprint-wrap-up)
- [📅 Sprint 2 Progress Tracker (Analytics Engine)](#-sprint-2-progress-tracker-analytics-engine)
  - [📈 Day 8: Profitability Ratios Implementation](#-day-8-profitability-ratios-implementation)
  - [⚖️ Day 9: Leverage & Efficiency Ratios](#️-day-9-leverage--efficiency-ratios)
  - [📊 Day 10: CAGR Calculation Engine](#-day-10-cagr-calculation-engine)
  - [💸 Day 11: Cash Flow KPIs & Allocation Patterns](#-day-11-cash-flow-kpis--allocation-patterns)
  - [🗄️ Day 12: Database Population & Core Ingestion](#️-day-12-database-population--core-ingestion)
- [📂 Repository Structure](#-repository-structure)
- [🛠️ Execution & Setup Guide](#️-execution--setup-guide)

---

## 🎯 Project Overview

This repository contains the Capstone Project for the **Bluestock Fintech Data Analytics Internship**.

The goal of this project is to build an end-to-end Financial Intelligence Platform analyzing data for the Nifty 100 companies. The project processes 12 source datasets (7 core and 5 supplementary) across 12 distinct modules over a 45-day execution plan.

**Sprints Completed:** `Sprint 1`

**Status:** `Sprint 2 - In Progress`

---

## 📅 Sprint 1 Progress Tracker (Data Foundation)

### 🔹 Day 01: Environment & Project Foundation
- **Directory Structure:** Established a professional workspace layout (`src/`, `tests/`, `data/`, `reports/`).
- **Virtual Environment:** Set up a clean Python virtual environment (`.venv`) to isolate dependencies.
- **Dependency Management:** Configured `requirements.txt` with core data science and analytical libraries including Pandas, Pytest, Pytest-HTML, Streamlit, etc.
- **Environment Variables:** Set up `.env` for managing sensitive configurations like database paths and ports.
- **Automation:** Created a custom `Makefile` for running shortcuts and a Windows batch script (`activate_env.bat`) for quick environment activation.
- **System Integration:** Successfully resolved and configured GnuWin32 `make` tool utility paths on Windows PowerShell.

### 🔹 Day 02: Data Loader & Normalizer Engine
- **Normalizer Logic (`src/etl/normaliser.py`):** Developed robust data cleansing functions:
  - `normalize_ticker()`: Standardizes all variations of company names/tickers to strict uppercase.
  - `normalize_year()`: Converts scattered year strings (`Mar-23`, `FY24`, `2023`) into a single uniform financial period format (`YYYY-MM`).
- **Data Loading Pipeline (`src/etl/loader.py`):** Programmed an automated pipeline using `pandas` to read complex core Excel financial files, strip metadata, and auto-apply normalization rules.
- **Unit Test Suite (`tests/etl/test_normalise.py`):** Authored 23 rigorous unit tests evaluating edge cases for year parsing and ticker string formatting.
- **Test Execution:** Fully integrated `pytest` with `make test`, generating comprehensive HTML reports with **100% passing results (23/23 tests passed)**.

### 🔹 Day 03: Schema Validator (16 DQ Rules)
- **Data Quality Engine (`src/etl/validator.py`):** Developed a robust data validation class to ensure data integrity across the pipeline.
- **Rule Implementation:** Successfully coded critical checks including PK/FK uniqueness (DQ-01, DQ-02), Balance Sheet tally verification (DQ-04), and Positive Sales validation (DQ-06).
- **Error Logging:** Configured the system to automatically flag violations and export them to `reports/validation_failures.csv`.

### 🔹 Day 04: Database Schema Engineering
- **Schema Design (`src/etl/schema.sql`):** Architected the foundational SQLite Star Schema layout for the financial warehouse.
- **Table Creation:** Written strict DDL statements for 12 tables including `companies`, `profitandloss`, `balancesheet`, and `stock_prices`.
- **Data Integrity:** Enforced `PRAGMA foreign_keys = ON` and established primary/foreign key relationships to maintain standard data normalization.

### 🚀 Day 05: Database Loader Pipeline
- **Objective:** Ingest all 12 validated Excel datasets into a centralized SQLite database.
- **Actions:**
  - Developed `src/etl/loader.py` to handle automated table creation and data insertion.
  - Executed schema initialization using `schema.sql`.
  - Successfully loaded data into all 12 tables (`companies`, `profitandloss`, `stock_prices`, etc.).
  - Managed table dependencies (Foreign Keys) by ensuring correct load order.
  - Generated a load audit report (`reports/load_audit.csv`) confirming the successful insertion of all records.

### 🧐 Day 06: Data Quality Manual Review
- **Objective:** Perform manual checks on the loaded SQLite database to ensure data integrity.
- **Actions:**
  - Created a temporary `manual_review.py` script.
  - Queried 5 random companies to verify the `companies` table data structure.
  - Checked for minimum year coverage (P&L data). Successfully identified newly listed companies like `JIOFIN` having less than 5 years of data.
  - Confirmed that the ETL pipeline is bug-free and the database is ready for the Analytics phase.

### 🏁 Day 07: Sprint Wrap-Up
- **Objective:** Ensure pipeline stability, zero data loss, and finalize Sprint 1.
- **Actions:**
  - Executed 10 exploratory SQL queries directly on `nifty100.db` using `exploratory_queries.sql` to verify data completeness and table relationships.
  - Expanded Pytest unit test coverage to 38 tests (100% pass rate) across `normaliser.py` and `validator.py`.
  - Completed end-to-end Sprint 1 retrospective. The data foundation is solid and ready for the Analytics Engine.

---

## 📅 Sprint 2 Progress Tracker (Analytics Engine)

### 📈 Day 08: Profitability Ratios Implementation
- **Objective:** Program core profitability ratios to measure company financial health.
- **KPIs Computed:** Net Profit Margin (NPM), Operating Profit Margin (OPM), Return on Equity (ROE), and Return on Capital Employed (ROCE).
- **Edge Case Handling:**
  - Handled negative equity scenarios (returning `None` for ROE).
  - Handled zero sales scenarios (returning `None` for NPM and OPM to avoid `ZeroDivisionError`).
- **Validation:** Cross-verified calculated OPM values against original source files (`opm_percentage`). Detected expected anomalies in banking/financial sectors.
- **Deliverable:** `src/analytics/ratios.py`

### ⚖️ Day 09: Leverage & Efficiency Ratios
- **Objective:** Build metrics to evaluate corporate debt levels and asset utilization efficiency.
- **KPIs Computed:** Debt-to-Equity (D/E) Ratio, Interest Coverage Ratio (ICR), and Asset Turnover Ratio.
- **Edge Case Handling:**
  - Developed a Bank Carve-out logic matching company IDs to systematically bypass standard D/E calculations for financial institutions.
  - Implemented Debt-free substitution (assigning `999.0` for ICR) to prevent errors on companies with zero interest.
- **Validation:** Authored and passed 5 comprehensive unit tests targeting leverage edge cases.
- **Deliverable:** Updated `src/analytics/ratios.py` and new `tests/kpi/test_leverage.py`.

### 📊 Day 10: CAGR Calculation Engine
- **Objective:** Engineer a Compound Annual Growth Rate (CAGR) calculator for evaluating long-term company performance.
- **KPIs Computed:** Revenue CAGR, PAT CAGR, and EPS CAGR computed across multiple sliding windows (3Y, 5Y, and 10Y).
- **Edge Case Handling:**
  - Integrated "Turnaround Flag Logic" to identify companies transitioning from negative to positive net profit.
  - Solved `RuntimeWarning` exceptions by securely bypassing fractional power calculations on negative bases.
- **Deliverable:** `src/analytics/cagr.py`

### 💸 Day 11: Cash Flow KPIs & Allocation Patterns
- **Objective:** Analyze cash flow statements to determine liquidity indicators and capital allocation strategies.
- **KPIs Computed:** Free Cash Flow (FCF), CFO Quality Score, CapEx Intensity, and FCF Conversion Ratio.
- **Pattern Classification:** Developed a proprietary algorithm to classify companies into 8 Capital Allocation Patterns (e.g., Mature/Cash Cow, High Burn/Startup) based on the polarity of Operating, Investing, and Financing cash flows.
- **Deliverable:** `src/analytics/cashflow_kpis.py`

### 🗄️ Day 12: Database Population & Core Ingestion
- **Objective:** Aggregate all calculated analytics and ingest them into the primary SQLite database.
- **Actions:**
  - Executed the Profitability, CAGR, and Cash Flow engines simultaneously.
  - Merged outputs into a master DataFrame using `company_id` and `year` as composite keys to ensure data integrity.
  - Uploaded 1,467 processed rows to the new `financial_ratios` table in `nifty100.db`.
  - Conducted random sample cross-verification against raw manual Excel calculations.
- **Deliverable:** `src/analytics/populate_ratios.py` and updated `nifty100.db`.

---

## 📂 Repository Structure

```text
📦N100 FINANCIAL INTELLIGENCE PLATFORM
 ┣ 📂data
 ┃ ┣ 📂raw                         # 7 core Excel files (READ ONLY). Never modify.
 ┃ ┗ 📂supporting                  # 5 supplementary Excel files.
 ┣ 📜nifty100.db                   # Primary SQLite database containing all tables.
 ┣ 📂src
 ┃ ┣ 📂etl                         # Extraction, Transformation, and Loading
 ┃ ┃ ┣ 📜exploratory_queries.sql   # Exploratory queries for DB manual checks
 ┃ ┃ ┣ 📜normaliser.py             # Data cleaning logic
 ┃ ┃ ┣ 📜loader.py                 # Excel reading and DB loading logic
 ┃ ┃ ┣ 📜validator.py              # Data Quality Rules
 ┃ ┃ ┗ 📜schema.sql                # Database Schema definition
 ┃ ┣ 📂analytics                   # Ratios, CAGR, Screener engines, etc.
 ┃ ┃ ┣ 📜ratios.py                 # Profitability, Leverage & Efficiency Ratios
 ┃ ┃ ┣ 📜cagr.py                   # Compound Annual Growth Rate engine
 ┃ ┃ ┣ 📜cashflow_kpis.py          # Cash flow metrics & Pattern classification
 ┃ ┃ ┗ 📜populate_ratios.py        # Master ingestion script to SQLite
 ┃ ┣ 📂nlp                         # Parsers and pros/cons generators
 ┃ ┣ 📂dashboard                   # Streamlit app and modular pages
 ┃ ┣ 📂api                         # FastAPI server routers
 ┃ ┗ 📂reports                     # Report generation scripts (Tearsheets, Sector)
 ┣ 📂tests                         # Pytest test files (43 tests total)
 ┃ ┣ 📂etl
 ┃ ┃ ┣ 📜test_normalise.py         # 23 passing unit tests for Normalizer
 ┃ ┃ ┗ 📜test_validator.py         # 15 passing unit tests for DQ Validator
 ┃ ┗ 📂kpi
 ┃   ┗ 📜test_leverage.py          # 5 passing unit tests for Day 09 edge cases
 ┣ 📂config                        # YAML configurations and .env templates
 ┣ 📂reports                       # Generated HTML/CSV reports and PDFs
 ┃ ┣ 📜pytest_report.html          # Pytest HTML execution results
 ┃ ┣ 📜load_audit.csv              # Database load audit report
 ┃ ┗ 📜validation_failures.csv     # Data quality validation failures
 ┣ 📂output                        # Screener exports, ad-hoc CSVs, final archives
 ┣ 📂notebooks                     # Exploratory Jupyter notebooks
 ┣ 📂docs                          # Project documents, analyst guides, OpenAPI specs
 ┣ 📜.env                          # Environment variables
 ┣ 📜Makefile                      # Automation targets (load, test, api, dashboard)
 ┣ 📜requirements.txt              # Standard system dependencies
 ┗ 📜activate_env.bat              # Quick environment activation script

```
---


## 🛠️ Execution & Setup Guide

### 1. System Deployment & Virtual Environment Setup

Activate the Python dependency environment:

```powershell
.\activate_env.bat
```

### 2. Run the Data Loader

Execute the loader pipeline to read and normalize the raw Excel files:

```bash
make load
```

### 3. Execute Unit Tests & Generate Report

Run the comprehensive unit test suite to validate the normalization logic:

```bash
make test
```

### 4. Verify the HTML Test Report

Open the generated file at `reports/pytest_report.html` in any web browser to see the professional pipeline audit execution results.

### 5. Run the Analytics Engine (Profitability Ratios)

Execute the scripts to calculate Ratios and CAGR metrics:

```bash
python -m src.analytics.ratios
python -m src.analytics.cagr
```

### 6. Run the Analytics Engines & Populate Database

Execute the master population script to run all analytical modules and ingest data into SQLite:

```bash
python -m src.analytics.populate_ratios
```