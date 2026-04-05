import pandas as pd
import plotly.express as px


# Step 1: Load cleaned dataset

df = pd.read_csv("cleaned_weather.csv")

print("Dataset Loaded Successfully")
print("Shape:", df.shape)


# Step 2: Dataset Overview

"""
Displays column names and datatypes.
Helps understand data schema.
"""
print("\nDataset Info:\n")
print(df.info())


# Step 3: Statistical Summary

"""
Provides mean, min, max, std deviation for numeric columns.
"""
print("\nStatistical Summary:\n")
print(df.describe())


# Insight 1: Global Temperature Distribution

"""
Histogram showing overall temperature spread.
"""
fig1 = px.histogram(
    df,
    x="temperature_celsius",
    nbins=40,
    title="Global Temperature Distribution"
)
fig1.show()


# Insight 2: Average Temperature by Country

"""
Groups data by country to identify regional climate differences.
"""
country_temp = df.groupby("country")["temperature_celsius"].mean().reset_index()

fig2 = px.choropleth(
    country_temp,
    locations="country",
    locationmode="country names",
    color="temperature_celsius",
    title="Average Temperature by Country"
)
fig2.show()


# Insight 3: Seasonal Temperature Trend

"""
Extract month from date and compute monthly average temperature.
"""
df["last_updated"] = pd.to_datetime(df["last_updated"])
df["month"] = df["last_updated"].dt.month

monthly_temp = df.groupby("month")["temperature_celsius"].mean().reset_index()

fig3 = px.line(
    monthly_temp,
    x="month",
    y="temperature_celsius",
    title="Monthly Average Temperature Trend"
)
fig3.show()


# Insight 4: Temperature vs Humidity

"""
Scatter plot to observe correlation between temperature and humidity.
"""
fig4 = px.scatter(
    df,
    x="temperature_celsius",
    y="humidity",
    title="Temperature vs Humidity Correlation"
)
fig4.show()


# Insight 5: Top 10 Highest Rainfall Countries

"""
Identifies countries with highest average precipitation.
"""
rain = df.groupby("country")["precip_mm"].mean().reset_index()
rain = rain.sort_values(by="precip_mm", ascending=False).head(10)

print("\nTop 10 Highest Rainfall Countries:\n")
print(rain)


# Insight 6: Top 10 Highest Wind Speed Countries

"""
Detects regions prone to strong winds.
"""
wind = df.groupby("country")["wind_kph"].mean().reset_index()
wind = wind.sort_values(by="wind_kph", ascending=False).head(10)

print("\nTop 10 Highest Wind Speed Countries:\n")
print(wind)


# Insight 7: Correlation Matrix

"""
Shows relationships between numeric weather parameters.
"""
correlation = df.corr(numeric_only=True)

print("\nCorrelation Matrix:\n")
print(correlation)

print("\nAll insights generated successfully.")