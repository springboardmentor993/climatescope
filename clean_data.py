"""
ClimateScope – Global Weather Data Cleaning Script

This script cleans the raw GlobalWeatherRepository dataset by:
1. Loading the CSV file
2. Standardizing column names
3. Removing duplicate records
4. Handling missing values (numeric + categorical)
5. Removing extreme temperature outliers
6. Saving a cleaned dataset

Author: Akshat Raj Pathak
"""

import pandas as pd

# -------------------------------------------------
# Step 1: Load Dataset
# -------------------------------------------------
df = pd.read_csv("GlobalWeatherRepository.csv")

print("\nDataset loaded successfully.")
print("Original Shape:", df.shape)

# Preview data
print("\nFirst 5 rows:\n")
print(df.head())

# -------------------------------------------------
# Step 2: Standardize Column Names First
# (lowercase + replace spaces with underscores)
# -------------------------------------------------
df.columns = df.columns.str.lower().str.replace(" ", "_")

# -------------------------------------------------
# Step 3: Remove Duplicate Rows
# -------------------------------------------------
df = df.drop_duplicates()
print("\nAfter removing duplicates:", df.shape)

# -------------------------------------------------
# Step 4: Check Missing Values
# -------------------------------------------------
print("\nMissing Values Before Cleaning:\n")
print(df.isnull().sum())

# -------------------------------------------------
# Step 5: Handle Missing Values
# Numeric columns → fill with mean
# Text columns → fill with 'Unknown'
# -------------------------------------------------
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
categorical_cols = df.select_dtypes(include=["object"]).columns

df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
df[categorical_cols] = df[categorical_cols].fillna("Unknown")

# -------------------------------------------------
# Step 6: Convert Date Column if Present
# -------------------------------------------------
if "last_updated" in df.columns:
    df["last_updated"] = pd.to_datetime(df["last_updated"], errors="coerce")

# -------------------------------------------------
# Step 7: Remove Unrealistic Temperature Outliers
# -------------------------------------------------
if "temperature_celsius" in df.columns:
    before = df.shape[0]

    df = df[
        (df["temperature_celsius"] >= -50) &
        (df["temperature_celsius"] <= 60)
    ]

    after = df.shape[0]
    print(f"\nRemoved {before - after} temperature outliers.")

# -------------------------------------------------
# Step 8: Final Missing Value Check
# -------------------------------------------------
print("\nMissing Values After Cleaning:\n")
print(df.isnull().sum())

# -------------------------------------------------
# Step 9: Save Cleaned Dataset
# -------------------------------------------------
df.to_csv("cleaned_weather.csv", index=False)

print("\nCleaned dataset saved as cleaned_weather.csv")
print("Final Shape:", df.shape)

print("\nData Cleaning Completed Successfully.")