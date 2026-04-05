"""
ClimateScope – Monthly Aggregation Script

This script converts cleaned daily weather data into monthly averages.

Why aggregation?
-----------------
Raw data contains daily records, which are large and noisy.
Monthly aggregation:

1. Reduces dataset size
2. Removes daily fluctuations
3. Highlights seasonal trends
4. Makes visualization clearer
5. Prepares data for dashboard and analysis

Input File:
-----------
cleaned_weather.csv

Output File:
------------
monthly_weather.csv

Author: Akshat Raj Pathak
"""

import pandas as pd

# ---------------------------------------------------------
# Step 1: Load the cleaned dataset
# ---------------------------------------------------------
# Reads cleaned_weather.csv into pandas DataFrame
df = pd.read_csv("cleaned_weather.csv")

print("Cleaned dataset loaded successfully.")
print("Original Shape:", df.shape)

# ---------------------------------------------------------
# Step 2: Convert 'last_updated' column to datetime format
# ---------------------------------------------------------
# This allows extraction of year and month for aggregation
df["last_updated"] = pd.to_datetime(df["last_updated"], errors="coerce")

# ---------------------------------------------------------
# Step 3: Create new time-based features
# ---------------------------------------------------------
# Extract year from date
df["year"] = df["last_updated"].dt.year

# Extract month from date
df["month"] = df["last_updated"].dt.month

print("Year and Month extracted from date.")

# ---------------------------------------------------------
# Step 4: Perform Monthly Aggregation
# ---------------------------------------------------------
"""
Group data by:
- country
- year
- month

Then calculate MEAN for all numeric columns.

This converts daily weather values into monthly averages,
making it easier to study climate trends.
"""
monthly_df = (
    df
    .groupby(["country", "year", "month"])
    .mean(numeric_only=True)
    .reset_index()
)

print("Monthly aggregation completed.")
print("Aggregated Shape:", monthly_df.shape)

# ---------------------------------------------------------
# Step 5: Save aggregated dataset
# ---------------------------------------------------------
# Export monthly averaged data to CSV
monthly_df.to_csv("monthly_weather.csv", index=False)

print("monthly_weather.csv saved successfully.")

# ---------------------------------------------------------
# Step 6: Display preview of aggregated data
# ---------------------------------------------------------
print("\nFirst 5 rows of monthly aggregated data:\n")
print(monthly_df.head())

print("\nAggregation process completed successfully.")