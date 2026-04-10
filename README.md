# 🌍 ClimateScope Dashboard  

An interactive data visualization dashboard for analyzing global climate patterns using dynamic filters and rich visual analytics.

---

##  Overview  

The **ClimateScope Dashboard** is designed to help users explore and understand climate data across different countries, seasons, and time periods. It transforms raw environmental data into meaningful insights through interactive charts and visualizations.

---

##  Features  

-  Multi-filter selection (Country, Year Range, Season)  
-  KPI summary (Temperature, Humidity, Rainfall)  
-  Trend analysis over time  
-  Seasonal comparison  
-  Regional analysis using maps  
-  Extreme climate event detection  
-  Data distribution visualization  
-  Correlation heatmap  
-  Filtered dataset preview  

---

##  Dashboard Sections  

- **Filters Panel** – Select country, year, season, and metric  
- **KPI Cards** – Quick overview of key climate metrics  
- **Trends Tab** – Year-wise analysis  
- **Seasonal Tab** – Seasonal comparisons  
- **Regional Tab** – Country-level insights with maps  
- **Extremes Tab** – Detection of extreme conditions  
- **Distribution Tab** – Data spread visualization  
- **Correlation Section** – Relationship between variables  
- **Data Preview** – Tabular data view  

---

##  Tech Stack  

- **Frontend:** Streamlit  
- **Data Processing:** Pandas  
- **Visualization:** Plotly, Matplotlib, Seaborn  
- **Language:** Python  

---

##  Project Structure 
```
  project/
  │── data/
  │     └── weather_cleaned_with_seasons.csv
  │── app.py
  │── dashboard_design.md
  │── requirements.txt
  │── README.md
  └── LICENSE
 
 ```
---
##  How to Run
1. Install dependencies:
```
   pip install -r requirements.txt
```
2. Run the app:
```
   streamlit run app.py
```
---

##  Dataset  

The dataset contains climate-related attributes such as:
- Country  
- Year  
- Season  
- Temperature (°C)  
- Humidity (%)  
- Precipitation (mm)  
- Wind Speed (kph)  
- Pressure (mb)
  A sample dataset is included in this repository for demonstration and testing purposes.
---

##  Deployment  

The dashboard is designed to be deployed on cloud platforms such as Streamlit Cloud, enabling users to access and interact with the application through a web browser without local setup.

Live Demo: https://climatescope-ilpeft4uryrdboowcosoch.streamlit.app/

---

##  Future Enhancements  

- Integration with real-time climate APIs  
- Machine learning-based predictions  
- Advanced analytics and forecasting  

---

##  License  

This project is licensed under the MIT License.

---

##  Acknowledgment  

This project was developed as part of an internship to demonstrate skills in data analysis, visualization, and dashboard development.
