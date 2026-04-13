import pandas as pd


df = pd.read_csv("./data/GlobalWeatherRepository.csv")

print("Dataset Info:")
print(df.info())


print("\nFirst 5 rows:")
print(df.head())

print("\nMissing Values per Column:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

print("\nUnique Countries:")
print(df['country'].unique())

print("\nUnique Locations (first 20):")
print(df['location_name'].unique()[:20])


print("\nDuplicate Rows:", df.duplicated().sum())
df = df.drop_duplicates()


df['last_updated'] = pd.to_datetime(df['last_updated'])


df_clean = df.copy()


df_clean = df_clean.drop(columns=['temperature_fahrenheit', 'feels_like_fahrenheit'])


df_clean = df_clean.drop(columns=['wind_mph', 'gust_mph'])


df_clean = df_clean.drop(columns=['precip_in'])


df_clean = df_clean.drop(columns=['visibility_miles'])


df_clean = df_clean.drop(columns=['pressure_in'])

df_clean.to_csv("./data/cleaned_weather.csv", index=False)
print("Cleaned dataset saved successfully!")


df_clean['month'] = df_clean['last_updated'].dt.to_period('M')


monthly = df_clean.groupby(['month', 'country', 'location_name']).agg('mean', numeric_only=True).reset_index()

print("\nMonthly Aggregated Data (first 10 rows):")
print(monthly.head(10))


monthly.to_csv("./data/monthly_weather.csv", index=False)
print("Monthly aggregated dataset saved successfully!")

eda_df = pd.read_csv("./data/monthly_weather.csv")

print("EDA Dataset Info:")
print(eda_df.info())

print("\nFirst 5 rows of EDA dataset:")
print(eda_df.head())

import matplotlib.pyplot as plt

countries_to_plot = ["India", "United States of America"]

for country in countries_to_plot:
    subset = eda_df[eda_df['country'] == country]
    plt.plot(subset['month'], subset['temperature_celsius'], label=country)

plt.xlabel("Month")
plt.ylabel("Avg Temperature (°C)")
plt.title("Monthly Temperature Trends")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


import seaborn as sns


countries_to_plot = ["India", "United States of America", "Australia"]

subset = eda_df[eda_df['country'].isin(countries_to_plot)]

plt.figure(figsize=(10,6))
sns.boxplot(x="country", y="humidity", data=subset)

plt.title("Humidity Distribution by Country")
plt.xlabel("Country")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt


countries_to_plot = ["India", "United States of America", "China"]

subset = eda_df[eda_df['country'].isin(countries_to_plot)]

plt.figure(figsize=(10,6))
sns.barplot(x="country", y="air_quality_PM2.5", data=subset, errorbar=None)
plt.title("Average PM2.5 Levels by Country")
plt.xlabel("Country")
plt.ylabel("PM2.5 Concentration")
plt.tight_layout()
plt.show()



import seaborn as sns
import matplotlib.pyplot as plt


corr = eda_df.corr(numeric_only=True)

plt.figure(figsize=(12,8))
sns.heatmap(corr, cmap="coolwarm", annot=False)

plt.title("Correlation Heatmap of Weather Variables")
plt.tight_layout()
plt.show()




import matplotlib.pyplot as plt


india_data = eda_df[eda_df['country'] == "India"]

plt.figure(figsize=(10,6))
plt.plot(india_data['month'], india_data['temperature_celsius'], label="Temperature (°C)", color="red")
plt.plot(india_data['month'], india_data['humidity'], label="Humidity (%)", color="blue")

plt.xlabel("Month")
plt.ylabel("Values")
plt.title("Seasonal Trends in India")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



import seaborn as sns
import matplotlib.pyplot as plt


india_data = eda_df[eda_df['country'] == "India"]

plt.figure(figsize=(10,6))
sns.boxplot(x=india_data['temperature_celsius'])

plt.title("Temperature Outliers in India")
plt.xlabel("Temperature (°C)")
plt.tight_layout()
plt.show()


plt.figure(figsize=(10,6))
sns.boxplot(x=india_data['air_quality_PM2.5'])

plt.title("PM2.5 Outliers in India")
plt.xlabel("PM2.5 Concentration")
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

india_data = eda_df[eda_df['country'] == "India"].copy()


india_data['month_dt'] = pd.to_datetime(india_data['month'])

india_data['month_num'] = np.arange(len(india_data))

X = india_data[['month_num']]
y = india_data['temperature_celsius']

# Train model
model = LinearRegression()
model.fit(X, y)


future_months = np.arange(india_data['month_num'].max()+1,
                          india_data['month_num'].max()+7).reshape(-1,1)
future_preds = model.predict(future_months)


last_date = india_data['month_dt'].max()
future_labels = pd.date_range(last_date + pd.offsets.MonthBegin(),periods=6, freq='M').strftime("%Y-%m")


plt.figure(figsize=(10,6))
plt.plot(india_data['month_dt'].dt.strftime("%Y-%m"), y,
         label="Actual Temperature", color="blue")
plt.plot(future_labels, future_preds,
         label="Forecast", color="red", linestyle="--")

plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Forecast for India")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

india_data = eda_df[eda_df['country'] == "India"]

plt.figure(figsize=(8,6))
sns.regplot(x="temperature_celsius", y="humidity", data=india_data, scatter_kws={"color":"blue"}, line_kws={"color":"red"})
plt.title("Temperature vs Humidity (India)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.show()


plt.figure(figsize=(8,6))
sns.regplot(x="air_quality_PM2.5", y="air_quality_PM10", data=india_data, scatter_kws={"color":"green"}, line_kws={"color":"orange"})
plt.title("PM2.5 vs PM10 (India)")
plt.xlabel("PM2.5 Concentration")
plt.ylabel("PM10 Concentration")
plt.tight_layout()
plt.show()

# Export cleaned dataset for Power BI

corr = eda_df[['temperature_celsius','humidity','air_quality_PM2.5','air_quality_PM10']].corr()
corr.to_csv("correlation_matrix.csv")








