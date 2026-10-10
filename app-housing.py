
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("housing.csv")

# App title
st.title("California Housing Data (1990) by Zhou Yunyi")

# Slider for minimum house value
min_value = st.slider(
    "Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000
)

# Filter by house value
filtered_df = df[df["median_house_value"] >= min_value]

# Subheader
st.subheader("See more filters in the sidebar:")

# Sidebar: location type
location_types = df["ocean_proximity"].unique()

selected_locations = st.sidebar.multiselect(
    "Choose the location type",
    options=location_types,
    default=location_types
)

# Filter by location type
filtered_df = filtered_df[
    filtered_df["ocean_proximity"].isin(selected_locations)
]

# Sidebar: income level
income_level = st.sidebar.radio(
    "Choose income level",
    ["Low", "Medium", "High"]
)

# Filter by income level
if income_level == "Low":
    filtered_df = filtered_df[
        filtered_df["median_income"] <= 2.5
    ]

elif income_level == "Medium":
    filtered_df = filtered_df[
        (filtered_df["median_income"] > 2.5) &
        (filtered_df["median_income"] < 4.5)
    ]

else:
    filtered_df = filtered_df[
        filtered_df["median_income"] >= 4.5
    ]

# Show map of filtered districts
st.map(filtered_df)

# Histogram of median house values
fig, ax = plt.subplots()

ax.hist(
    filtered_df["median_house_value"],
    bins=30
)

ax.set_xlabel("Median House Value")
ax.set_ylabel("Number of Districts")
ax.set_title("Distribution of Median House Values")

st.pyplot(fig)
