<div align="center">

# 📈 Nifty 100 Financial Intelligence Platform
### End-to-End Financial Analytics & Business Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-green?style=for-the-badge&logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Analytics-purple?style=for-the-badge&logo=pandas&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Sprint_1-In_Progress-yellow?style=for-the-badge)

<br>

---
</div>

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [📅 Sprint 1 Progress Tracker](#-sprint-1-progress-tracker)
- [🚀 Day 1: Environment & Project Foundation](#-day-1-environment--project-foundation)
- [🛠️ Day 2: Data Loader & Normalizer Engine](#️-day-2-data-loader--normalizer-engine)
- [🔍 Day 3: Schema Validator (16 DQ Rules)](#-day-3-schema-validator-16-dq-rules)
- [🗄️ Day 4: Database Schema Engineering](#️-day-4-database-schema-engineering)
- [📂 Repository Structure](#-repository-structure)
- [🛠️ Execution & Setup Guide](#️-execution--setup-guide)

---

## 🎯 Project Overview

This repository contains the Capstone Project for the **Bluestock Fintech Data Analytics Internship**.

The goal of this project is to build an end-to-end Financial Intelligence Platform analyzing data for the Nifty 100 companies. The project processes 12 source datasets (7 core and 5 supplementary) across 12 distinct modules over a 45-day execution plan.

**Sprints Completed:** `Sprint 1 (Day 1 to Day 4)`

**Status:** `Sprint 1 - In Progress`

---

## 📅 Sprint 1 Progress Tracker

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
- **Table Creation:** Written strict DDL statements for 10 core tables including `companies`, `profitandloss`, `balancesheet`, and `cashflow`.
- **Data Integrity:** Enforced `PRAGMA foreign_keys = ON` and established primary/foreign key relationships to maintain standard data normalization.

---

## 📂 Repository Structure

```text
📦Nifty100_Capstone_Project
 ┣ 📂data
 ┃ ┣ 📂raw                         # Immutable source assets & Excel files
 ┃ ┗ 📂supporting                  # Supplementary financial datasets
 ┣ 📂src
 ┃ ┣ 📂etl                         # Extraction, Transformation, and Loading
 ┃ ┃ ┣ 📜normaliser.py             # Data cleaning logic
 ┃ ┃ ┣ 📜loader.py                 # Excel reading logic
 ┃ ┃ ┗ 📜validator.py              # Data Quality Rules
 ┃ ┗ 📜schema.sql                  # Database Schema definition
 ┣ 📂tests
 ┃ ┗ 📂etl
 ┃   ┗ 📜test_normalise.py         # 23 passing unit tests
 ┣ 📂reports
 ┃ ┗ 📜pytest_report.html          # Pytest HTML execution results
 ┣ 📜.env                          # Environment configurations
 ┣ 📜Makefile                      # Automation targets (load, test, ratios, etc.)
 ┣ 📜requirements.txt              # Standard system dependencies
 ┣ 📜activate_env.bat              # Quick environment activation script
 ┗ 📜README.md
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