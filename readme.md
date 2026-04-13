ClimateScope Weather Dashboard — README
 Project Overview
This project focuses on analyzing global climate and air quality data and presenting it through an interactive Power BI dashboard. The goal is to study temperature, humidity, wind speed, precipitation, and pollution indicators across countries, with clear visuals and slicers for dynamic exploration.
The dataset (GlobalWeatherRepository_cleaned.csv) was cleaned and transformed using Python (EDA + preprocessing), and then modeled in Power BI for dashboard creation.

Project Structure
|–– 📄 CLIMATE_SCOPE.ipynb              # Python notebook for EDA + cleaning
|–– 📄 GlobalWeatherRepository_cleaned.csv  # Final cleaned dataset
|–– 📄 Aditya-climatescope dashboard.pbix   # Power BI dashboard file
|–– 📄 README.md                         # Documentation (this file)



 1. Data Cleaning & Preprocessing (Python)
Performed inside CLIMATE_SCOPE.ipynb using pandas, numpy, matplotlib, seaborn.
 Key Steps:
- Loaded raw dataset, inspected shape, datatypes, missing values, duplicates.
- Converted temperature from Fahrenheit → Celsius.
- Handled missing values (mean/median fill or column drop).
- Removed invalid entries (e.g., 500°C, negative humidity).
- Standardized time column → Year, Month, Day, Hour.
- Exported cleaned dataset → GlobalWeatherRepository_cleaned.csv.

 2. Exploratory Data Analysis (EDA)
EDA was done before cleaning to understand dataset behavior.
 Insights:
- Countries covered: 150+
- Summary statistics for temperature, humidity, wind, pressure.
- Outlier detection using boxplots & histograms.
- Correlation analysis (Temp vs Humidity, PM2.5 vs PM10, Wind vs Rainfall).
- Visualizations: distribution plots, heatmaps, line charts, bar charts.

 3. Power BI Dashboard
Final dashboard file → Aditya-climatescope dashboard.pbix.
 Visuals Included:
-  Temperature Trends → Avg, Max, Min per country + monthly line chart.
-  Humidity Analysis → Distribution + seasonal variation.
-  Wind & Rainfall → Gust vs Wind (Pie), Rainfall vs Wind (Combo chart).
-  Geo-Spatial Map → PM2.5 & PM10 pollution hotspots.
-  KPIs → Highest temp, lowest temp, avg humidity, avg wind speed.
-  Correlation Heatmap → Relationships between climate variables.
 Design Choices:
- Consistent color scheme (Blue = Temp, Green = Humidity, Red = PM2.5, Orange = PM10).
- Light background, clear fonts, tooltips for usability.
- Slicers for Country and Month, synced across pages.

 Dashboard Pages
- Page 1 → Global Climate Overview
- Page 2 → Renewable & Emissions Trends
- Page 3 → Map + Wind Analysis (newly added)

 Tools & Technologies
- Python (Colab/Jupyter) → Data cleaning, EDA
- pandas / numpy → Data manipulation
- matplotlib / seaborn → Visualizations
- Power BI Desktop → Dashboard creation
- CSV → Final dataset

 How to Use
- Open GlobalWeatherRepository_cleaned.csv for dataset view.
- Run CLIMATE_SCOPE.ipynb for EDA + cleaning steps.
- Open Aditya-climatescope dashboard.pbix in Power BI Desktop to explore visuals.

 Conclusion
This project demonstrates the complete workflow:
- Raw data → Cleaning → EDA → Dashboard
- Provides country-wise climate insights and highlights pollution + weather trends.
- Helps in understanding seasonal patterns, anomalies, and global climate behavior interactively
