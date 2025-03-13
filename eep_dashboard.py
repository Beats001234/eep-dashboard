import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Set page configuration for better UI
st.set_page_config(page_title="EEP Dashboard", layout="wide")

# Title of the dashboard
st.title("Ehindero Empowerment Project 2025 (EEP) Dashboard")
st.subheader("Tracking Initiatives Across Akoko North East & Akoko North West")

# List of Wards
wards = [
    "Okeagbe", "Ikare", "Ajowa", "Ikaramu", "Ese", "Arigidi", "Oyin", "Ibaram", "Gedegede", "Erusu",
    "Ogbagi", "Isua", "Ifira", "Ipe", "Epinmi", "Sosan", "Supare", "Oba", "Irun", "Akungba"
]

# Project Categories
categories = ["Education", "Healthcare", "Youth Empowerment", "Infrastructure", "Women & Community Development"]

# Generate Random Data for Projects
data = []
for ward in wards:
    for _ in range(random.randint(2, 4)):  # Each ward gets 2-4 projects
        data.append({
            "Ward": ward,
            "Project Name": f"{random.choice(categories)} Initiative",
            "Category": random.choice(categories),
            "Budget (₦M)": round(random.uniform(1, 10), 2),  # Random budget between ₦1M and ₦10M
            "Timeline": f"{random.choice(['Jan-Mar', 'Apr-Jun', 'Jul-Sep', 'Oct-Dec'])} 2025",
            "Impact (People)": random.randint(500, 5000)  # Random impact between 500 and 5000 people
        })

# Convert Data to DataFrame
df = pd.DataFrame(data)

# Sidebar Filters
st.sidebar.title("Filters")

# Filter by Project Category
category_filter = st.sidebar.selectbox("Filter by Category", ["All"] + categories)
if category_filter != "All":
    df = df[df["Category"] == category_filter]

# Display Data Table
st.subheader("Project Data Overview")
st.write(df)

# Budget Allocation by Ward (Bar Chart)
st.subheader("Budget Allocation by Ward")
fig_budget = px.bar(df, x="Ward", y="Budget (₦M)", color="Category", title="Budget Distribution")
st.plotly_chart(fig_budget, use_container_width=True)

# Project Distribution by Category (Pie Chart)
st.subheader("Project Distribution by Category")
fig_pie = px.pie(df, names="Category", title="Projects per Category")
st.plotly_chart(fig_pie)

# Impact Analysis by Ward (Heatmap / Scatter Plot)
st.subheader("Impact of Initiatives Across Wards")
fig_heatmap = px.scatter(
    df, x="Ward", y="Impact (People)", size="Impact (People)", color="Category", title="People Impacted per Ward"
)
st.plotly_chart(fig_heatmap, use_container_width=True)
