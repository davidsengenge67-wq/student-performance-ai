import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Student Performance AI", layout="wide")

# Load data
df = pd.read_csv("../data/student_data.csv")

st.title("Student Performance AI Dashboard")

# =========================
# ROW 1: DATA + STATS
# =========================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Dataset Preview")
    st.dataframe(df, use_container_width=True)

with col2:
    st.subheader("📌 Statistics")
    st.write(df.describe())

# =========================
# ROW 2: 3 GRAPHS
# =========================
st.subheader("Data Visualizations")

col3, col4, col5 = st.columns(3)

with col3:
    fig1, ax1 = plt.subplots()
    ax1.hist(df["marks"])
    ax1.set_title("Marks Distribution")
    st.pyplot(fig1, use_container_width=True)

with col4:
    fig2, ax2 = plt.subplots()
    ax2.scatter(df["hours"], df["marks"])
    ax2.set_title("Hours vs Marks")
    ax2.set_xlabel("Hours")
    ax2.set_ylabel("Marks")
    st.pyplot(fig2, use_container_width=True)

with col5:
    fig3, ax3 = plt.subplots()
    ax3.scatter(df["attendance"], df["marks"])
    ax3.set_title("Attendance vs Marks")
    ax3.set_xlabel("Attendance")
    ax3.set_ylabel("Marks")
    st.pyplot(fig3, use_container_width=True)

# =========================
# ROW 3: HEATMAP + INSIGHTS
# =========================
st.subheader("Advanced Analysis")

col6, col7 = st.columns(2)

with col6:
    fig4, ax4 = plt.subplots()
    sns.heatmap(df.corr(), annot=True, ax=ax4)
    ax4.set_title("Correlation Heatmap")
    st.pyplot(fig4, use_container_width=True)

with col7:
    st.subheader("Key Insights")

    avg_marks = df["marks"].mean()
    high = df[df["hours"] >= 3]["marks"].mean()
    low = df[df["hours"] < 3]["marks"].mean()

    att_high = df[df["attendance"] >= 70]["marks"].mean()
    att_low = df[df["attendance"] < 70]["marks"].mean()

    st.write("Average Marks:", round(avg_marks, 2))
    st.write("High Study Group:", round(high, 2))
    st.write("Low Study Group:", round(low, 2))
    st.write("Study Impact:", round(high - low, 2))

    st.write("Attendance Impact:", round(att_high - att_low, 2))