import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="ClimateScope Dashboard", layout="wide")

st.title("🌍 ClimateScope Dashboard")
st.caption("Interactive dashboard for analyzing global climate patterns")

# -----------------------------
# LOAD DATA (OPTIMIZED)
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/weather_cleaned_with_seasons.csv")

df = load_data()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🔍 Filters")

countries = st.sidebar.multiselect(
    "Select Country(s)",
    options=sorted(df["country"].unique())
)

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["year"].min()),
    int(df["year"].max()),
    (int(df["year"].min()), int(df["year"].max()))
)

seasons = st.sidebar.multiselect(
    "Select Season",
    options=df["season"].unique(),
    default=df["season"].unique()
)

metric = st.sidebar.selectbox(
    "Select Metric",
    ["temperature_celsius", "humidity", "precip_mm", "wind_kph"]
)

top_n = st.sidebar.slider("Top N Countries", 5, 20, 10)

# STOP if no selection
if not countries:
    st.warning("⚠️ Please select at least one country")
    st.info("Use the sidebar filters to explore climate data across regions, seasons, and time periods.")
    st.stop()

# -----------------------------
# FILTER DATA
# -----------------------------
filtered_df = df[
    (df["country"].isin(countries)) &
    (df["year"].between(year_range[0], year_range[1])) &
    (df["season"].isin(seasons))
]

# -----------------------------
# KPI SECTION
# -----------------------------
st.subheader("📊 Climate Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Temperature (°C)", round(filtered_df["temperature_celsius"].mean(), 2))
col2.metric("Avg Humidity (%)", round(filtered_df["humidity"].mean(), 2))
col3.metric("Avg Rainfall (mm)", round(filtered_df["precip_mm"].mean(), 2))

st.markdown("---")

# -----------------------------
# TABS
# -----------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Trends",
    "🌦 Seasonal",
    "🌍 Regional",
    "⚡ Extremes",
    "📊 Distribution"
])

# -----------------------------
# 📈 TRENDS
# -----------------------------
with tab1:
    st.subheader("📈 Climate Trends")

    trend = filtered_df.groupby("year")[metric].mean().reset_index()

    fig1 = px.line(trend, x="year", y=metric, markers=True)
    st.plotly_chart(fig1, use_container_width=True)

    st.info("📌 Insight: Trends reflect seasonal and long-term climate changes.")

# -----------------------------
# 🌦 SEASONAL
# -----------------------------
with tab2:
    st.subheader("🌦 Seasonal Analysis")

    col4, col5 = st.columns(2)

    seasonal_temp = filtered_df.groupby("season")["temperature_celsius"].mean().reset_index()
    fig2 = px.bar(seasonal_temp, x="season", y="temperature_celsius")

    col4.plotly_chart(fig2, use_container_width=True)

    seasonal_precip = filtered_df.groupby("season")["precip_mm"].mean().reset_index()
    fig3 = px.line(seasonal_precip, x="season", y="precip_mm", markers=True)

    col5.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# 🌍 REGIONAL (FIXED)
# -----------------------------
with tab3:
    st.subheader("🌍 Regional Analysis")

    country_compare = filtered_df.groupby("country")[metric].mean().reset_index() \
                                .sort_values(by=metric, ascending=False).head(top_n)

    fig_map = px.choropleth(
        country_compare,
        locations="country",
        locationmode="country names",
        color=metric
    )

    st.plotly_chart(fig_map, use_container_width=True)

    fig_bar = px.bar(country_compare, x="country", y=metric)
    st.plotly_chart(fig_bar, use_container_width=True)

    fig_scatter = px.scatter(
        filtered_df,
        x="pressure_mb",
        y="wind_kph",
        color="temperature_celsius"
    )

    st.plotly_chart(fig_scatter, use_container_width=True)

# -----------------------------
# ⚡ EXTREMES (FIXED)
# -----------------------------
with tab4:
    st.subheader("⚡ Extreme Events")

    extreme_temp = filtered_df[
        filtered_df["temperature_celsius"] > filtered_df["temperature_celsius"].quantile(0.95)
    ]

    if extreme_temp.empty:
        st.warning("No extreme temperature events found")
    else:
        fig = px.scatter(extreme_temp, x="temperature_celsius", y="humidity")
        st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# 📊 DISTRIBUTION (FIXED)
# -----------------------------
with tab5:
    st.subheader("📊 Distribution")

    fig1 = px.histogram(filtered_df, x="temperature_celsius")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.histogram(filtered_df, x="precip_mm", log_y=True)
    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# 🔗 CORRELATION
# -----------------------------
st.subheader("🔗 Correlation Analysis")

corr_data = filtered_df[[
    "temperature_celsius",
    "humidity",
    "wind_kph",
    "pressure_mb",
    "precip_mm"
]].corr()

fig_corr, ax = plt.subplots(figsize=(5, 3))
sns.heatmap(corr_data, annot=True, cmap="coolwarm", ax=ax)

colA, colB, colC = st.columns([1, 2, 1])
with colB:
    st.pyplot(fig_corr)

# -----------------------------
# DATA PREVIEW
# -----------------------------
st.subheader("📄 Data Preview")
st.dataframe(filtered_df.head(50))