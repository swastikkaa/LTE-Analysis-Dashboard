# LTE KPI Analysis Dashboard

Automated LTE KPI analysis dashboard built with **Python**, **Pandas**, **Matplotlib**, and **Streamlit** for comparing **pre- and post-network performance**.

## Overview

During my telecommunications analytics internship, one of my recurring responsibilities was generating **pre- and post-optimization LTE KPI reports** from multiple folders containing network performance CSV files.

The manual workflow required:
- Opening numerous KPI CSV reports
- Calculating performance metrics manually in Excel
- Consolidating results into a summary spreadsheet
- Comparing pre- and post-optimization performance

Generating a single report typically took **around two hours**.

To eliminate this repetitive workflow, I built an automated dashboard that processes KPI reports, calculates key LTE metrics, generates Excel reports, and visualizes network performance comparisons in **under two minutes**.

The tool was later reused to generate reports for additional network datasets during my internship.

# Dashboard Preview
## Dashboard Interface

<img width="1380" height="751" alt="image" src="https://github.com/user-attachments/assets/8c51a58b-a9f5-4fb7-ac67-f3adb905b517" />


## KPI Comparison

<img width="1344" height="1295" alt="image" src="https://github.com/user-attachments/assets/e2465f3e-d980-4be1-b0aa-3cf3797a4ccc" />




<img width="2518" height="1008" alt="image" src="https://github.com/user-attachments/assets/e5958aad-20f4-48d1-8b53-8f79efd6a7b3" />

## KPI Visualization

<img width="1538" height="1067" alt="image" src="https://github.com/user-attachments/assets/607568fd-5354-4ef1-8783-aa3b5b9557b3" />


# Features

- Automated LTE KPI calculation
- Pre vs Post network performance comparison
- Automatic CSV report discovery
- Excel report generation
- Interactive Streamlit dashboard
- KPI visualization using Matplotlib
- Modular Python architecture
- Synthetic sample dataset included for testing

# KPIs Calculated

The dashboard currently calculates:

- Call Setup Success Ratio (CSSR)
- Dropped Call Ratio (DCR)
- Call Setup Time (CST)
- SRVCC Handover Success Rate
- Voice Call Initiation (VCI)
- Attach Call Setup Success Ratio (ACSSR)
- RRC Drop Call Ratio
- ERAB Establishment Success Rate
- Mean User Data Rate (Download)
- Mean User Data Rate > 5 Mbps
- Mean User Data Rate (Upload)
- Mean User Data Rate > 0.2 Mbps
- Percentage of Download Samples ≥ 1 Mbps


# Project Structure

```text
LTE-Analysis-Dashboard/
│
├── analysis.py
├── constants.py
├── dashboard.py
├── loader.py
├── main.py
├── plots.py
├── requirements.txt
│
├── Synthetic Dataset/
│   ├── pre/
│   └── post/
│
└── README.md
```

# Technologies Used

- Python
- Pandas
- Streamlit
- Matplotlib
- OpenPyXL

# Installation

Clone the repository

```bash
git clone https://github.com/swastikkaa/LTE-Analysis-Dashboard.git
```

Move into the project directory

```bash
cd LTE-Analysis-Dashboard
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run dashboard.py
```

# Usage

1. Launch the dashboard.
2. Select the **PRE** dataset folder.
3. Select the **POST** dataset folder.
4. Click **Run Analysis**.
5. View the comparison dashboard.
6. Excel reports are automatically generated.

# Sample Dataset

This repository contains a **fully synthetic LTE KPI dataset** for demonstration purposes.
The synthetic data preserves the original file structure and formatting required by the dashboard while containing no real network or customer information.

# Results

The dashboard automates KPI analysis by:

- Processing multiple LTE KPI report folders automatically
- Generating standardized Excel reports
- Producing pre/post comparison tables
- Visualizing KPI improvements

The automated workflow reduced report generation time from approximately **2 hours** to **under 2 minutes**.

# Future Improvements

- File upload support instead of folder paths
- Docker deployment
- Additional KPI visualizations
- Interactive filtering
- Export charts as images
- Configurable KPI definitions

# Disclaimer
This project was inspired by a real-world telecommunications analytics workflow I worked on during my internship. However, no proprietary code, data, or company resources were used or reproduced in this repository.
The dataset included here is entirely synthetic, generated using Claude (Anthropic) to mimic the structure and format of typical LTE KPI reports, without containing any real network, customer, or company-specific information. The analysis logic and dashboard were independently rebuilt from scratch for this public demonstration.
This repository does not represent, and should not be interpreted as, actual output, data, or intellectual property belonging to any employer.
