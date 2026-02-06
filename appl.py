import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page title
st.title("Food Delivery Trends and Customer Satisfaction Analysis")

# Load dataset
df = pd.read_csv("Food_Delivery_Times.csv")   # change name if your CSV is different

# Remove missing values
df = df.dropna()

# ===============================
# METRICS
# ===============================
st.subheader("Key Metrics")

avg_delivery = round(df['Delivery_Time_min'].mean(), 2)
st.metric("Average Delivery Time (minutes)", avg_delivery)

# ===============================
# DELIVERY TIME DISTRIBUTION
# ===============================
st.subheader("Delivery Time Distribution")

fig1, ax1 = plt.subplots()
ax1.hist(df['Delivery_Time_min'], bins=20)
ax1.set_xlabel("Delivery Time (minutes)")
ax1.set_ylabel("Number of Orders")
st.pyplot(fig1)

# ===============================
# TRAFFIC VS DELIVERY TIME
# ===============================
st.subheader("Traffic Level vs Delivery Time")

fig2, ax2 = plt.subplots()
sns.boxplot(x='Traffic_Level', y='Delivery_Time_min', data=df, ax=ax2)
st.pyplot(fig2)

# ===============================
# WEATHER VS DELIVERY TIME
# ===============================
st.subheader("Weather vs Delivery Time")

fig3, ax3 = plt.subplots()
sns.boxplot(x='Weather', y='Delivery_Time_min', data=df, ax=ax3)
st.pyplot(fig3)

# ===============================
# VEHICLE TYPE VS DELIVERY TIME
# ===============================
st.subheader("Vehicle Type vs Delivery Time")

fig4, ax4 = plt.subplots()
sns.boxplot(x='Vehicle_Type', y='Delivery_Time_min', data=df, ax=ax4)
st.pyplot(fig4)

# ===============================
# RAW DATA VIEW
# ===============================
st.subheader("Dataset Preview")
st.dataframe(df.head(10))
