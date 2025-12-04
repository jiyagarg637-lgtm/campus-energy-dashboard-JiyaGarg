# campus-energy-dashboard-JiyaGarg  
**Assignment:** End-to-End Energy Consumption Analysis and Visualization  
**Student:** Jiya Garg 

---

## Project Overview

This project analyzes electricity consumption data from multiple campus buildings to identify energy usage patterns and provide actionable insights to the facilities team. It involves reading raw meter data CSV files, performing data cleaning and validation, aggregating usage statistics, modeling buildings and meter readings using object-oriented programming, and generating a multi-chart dashboard visualization along with summary reports.

---

## Folder Structure

campus-energy-dashboard
├── main.py # Main Python script implementing all tasks
├── data/ # Contains raw CSV files (one per building)
│ ├── building_a.csv
│ ├── building_b.csv
├── output/ # Generated outputs (created by script)
│ ├── cleaned_energy_data.csv
│ ├── building_summary.csv
│ ├── summary.txt
│ └── dashboard.png
└── README.md # This documentation file

---

## Getting Started

### Prerequisites

- Libraries: pandas, matplotlib

Install required libraries with:
pip install pandas matplotlib

### Running the Program

From the root directory (where `main.py` exists), run: python main.py


This will:

- Load and validate CSV data from the `data/` folder
- Perform daily and weekly aggregations
- Generate OOP-based building reports
- Create a multi-chart energy dashboard `output/dashboard.png`
- Export cleaned data and summary CSVs to `output/`
- Write an executive summary text to `output/summary.txt`

---

## Project Features

- Automatic ingestion and cleaning of multiple building CSV files
- Time-series aggregation for daily and weekly electricity totals
- Building-wise energy consumption summaries using custom classes
- Multi-chart visualization with trend lines, bar charts, and scatter plots
- Export of clean data, summary stats, visual dashboard, and text report
- Robust handling of missing or corrupt data files

---

## Sample Data Format

CSV files in `/data/` should have at least these columns:

- `timestamp` (e.g., 2025-01-01 00:00)
- `kwh` (electricity consumed)
- Optional: `building` name;

---

## Insights and Usage

The generated dashboard and reports help facility managers identify:

- Which buildings consume the most energy
- Peak hours and daily/weekly usage trends
- Opportunities for targeted energy-saving interventions

---
"C:\Users\Karan Chandna\OneDrive\Pictures\Screenshots\Screenshot 2025-12-04 225006.png"
