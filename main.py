# Task 1: Data Ingestion and Validation

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import os


def load_all_data():
    data_folder = Path("data/")

    # Only load these two files (changed as you requested)
    csv_files = [
        data_folder / "building_a.csv",
        data_folder / "building_b.csv"
    ]

    all_data = []

    for file in csv_files:
        try:
            df = pd.read_csv(file)
            df["building"] = file.stem  # building_a / building_b

            if "timestamp" not in df.columns:
                print(f"Missing timestamp column in {file}, skipping file.")
                continue

            if "kwh" not in df.columns:
                print(f"Missing kwh column in {file}, skipping file.")
                continue

            all_data.append(df)

        except Exception as e:
            print(f"Error reading {file}: {e}")

    if not all_data:
        print("No valid CSV files loaded.")
        return None

    df_combined = pd.concat(all_data, ignore_index=True)
    return df_combined



# Task 2: Core Aggregation Logic

def calculate_daily_totals(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    daily = df.resample("D", on="timestamp")["kwh"].sum()
    return daily


def calculate_weekly_totals(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    weekly = df.resample("W", on="timestamp")["kwh"].sum()
    return weekly


def building_wise_summary(df):
    summary = df.groupby("building")["kwh"].agg(["mean", "min", "max", "sum"])
    return summary



# Task 3: Object-Oriented Modeling

class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh


class Building:
    def __init__(self, name):
        self.name = name
        self.meter_readings = []

    def add_reading(self, timestamp, kwh):
        self.meter_readings.append(MeterReading(timestamp, kwh))

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.meter_readings)


class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def add_building(self, name):
        self.buildings[name] = Building(name)

    def get(self, name):
        return self.buildings.get(name)



# Task 4: Visual Output with Matplotlib

def create_dashboard(daily, weekly, summary):

    fig, ax = plt.subplots(1, 3, figsize=(16, 5))

    ax[0].plot(daily.index, daily.values)
    ax[0].set_title("Daily Consumption")
    ax[0].set_xlabel("Date")
    ax[0].set_ylabel("kWh")

    ax[1].bar(weekly.index, weekly.values)
    ax[1].set_title("Weekly Consumption")
    ax[1].set_xticklabels(weekly.index.strftime('%Y-%m-%d'), rotation=45)

    ax[2].scatter(summary["mean"], summary["max"])
    for building, row in summary.iterrows():
        ax[2].annotate(building, (row["mean"], row["max"]))

    ax[2].set_title("Mean vs Max Consumption")
    ax[2].set_xlabel("Mean")
    ax[2].set_ylabel("Max")

    plt.tight_layout()
    os.makedirs("output", exist_ok=True)
    plt.savefig("output/dashboard.png")
    print("Dashboard saved as output/dashboard.png")



# Task 5: Persistence and Executive Summary

def save_outputs(df, summary):
    os.makedirs("output", exist_ok=True)

    df.to_csv("output/cleaned_energy_data.csv", index=False)
    summary.to_csv("output/building_summary.csv")
    print("CSV files saved in output folder.")


def write_summary_file(summary):
    total = summary["sum"].sum()
    highest = summary["sum"].idxmax()

    with open("output/summary.txt", "w") as f:
        f.write("ENERGY USAGE SUMMARY REPORT\n")
        f.write("-----------------------------------\n")
        f.write(f"Total Campus Consumption: {total} kWh\n")
        f.write(f"Highest Consuming Building: {highest}\n")

    print("Summary.txt file generated.")



# Main Execution

df = load_all_data()

if df is not None:
    daily = calculate_daily_totals(df)
    weekly = calculate_weekly_totals(df)
    summary = building_wise_summary(df)

    create_dashboard(daily, weekly, summary)
    save_outputs(df, summary)
    write_summary_file(summary)

    print("All tasks completed successfully!")
else:
    print("Pipeline stopped. No valid data loaded.")
