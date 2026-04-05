#Task 1: Seasonal Research (Country-wise)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")


df = pd.read_csv("monthly_weather.csv")

print("Dataset Loaded Successfully")
print("Shape:", df.shape)



#  Create Season Column


df["month"] = df["month"].astype(int)

def get_season(month):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    else:
        return "autumn"

df["season"] = df["month"].apply(get_season)

print("Season column created successfully!")



#  FULL SEASONAL TABLES (ALL COUNTRIES)



print("FULL SEASONAL TEMPERATURE TABLE")


season_temp_full = (
    df.groupby(["country", "season"])["temperature_celsius"]
    .mean()
    .unstack()
)

print(season_temp_full)



print("FULL SEASONAL PRECIPITATION TABLE")


season_rain_full = (
    df.groupby(["country", "season"])["precip_mm"]
    .mean()
    .unstack()
)

print(season_rain_full)



print("FULL SEASONAL HUMIDITY TABLE")


season_humidity_full = (
    df.groupby(["country", "season"])["humidity"]
    .mean()
    .unstack()
)

print(season_humidity_full)



print("FULL SEASONAL WIND SPEED TABLE")


season_wind_full = (
    df.groupby(["country", "season"])["wind_kph"]
    .mean()
    .unstack()
)

print(season_wind_full)



print("FULL SEASONAL PRESSURE TABLE")


season_pressure_full = (
    df.groupby(["country", "season"])["pressure_mb"]
    .mean()
    .unstack()
)

print(season_pressure_full)





#  CREATE SEASONAL SUMMARY FILE (AGGREGATED VALUES)


print("\nCreating seasonal summary file...")

seasonal_summary = df.groupby(["country", "season"]).agg(
    avg_temperature_celsius = ("temperature_celsius", "mean"),
    avg_precip_mm = ("precip_mm", "mean"),
    avg_humidity = ("humidity", "mean"),
    avg_wind_kph = ("wind_kph", "mean"),
    avg_pressure_mb = ("pressure_mb", "mean")
).reset_index()

# Save aggregated seasonal data
seasonal_summary.to_csv("seasonal_country_summary.csv", index=False)


# Find top 5 countries by temperature variation
temp_range = df.groupby("country")["temperature_celsius"] \
               .agg(lambda x: x.max() - x.min())

top5 = temp_range.sort_values(ascending=False).head(5).index

print("\nTop 5 Countries with Highest Seasonal Variation:")
print(top5)

filtered_df = df[df["country"].isin(top5)]

season_temp_top5 = (
    filtered_df.groupby(["country", "season"])["temperature_celsius"]
    .mean()
    .unstack()
)

plt.figure(figsize=(8,5))
sns.heatmap(season_temp_top5, annot=True, cmap="coolwarm")
plt.title("Seasonal Temperature (°C) - Top 5 Countries")
plt.show()