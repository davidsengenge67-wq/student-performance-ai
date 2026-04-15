import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Student Performance AI", layout="wide")

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("../data/student_data.csv")

# =========================
# SIDEBAR FILTERS
# =========================
st.sidebar.header("Filters")

min_hours = st.sidebar.slider("Minimum Study Hours", 0, int(df["hours"].max()), 0)
min_att = st.sidebar.slider("Minimum Attendance", 0, int(df["attendance"].max()), 0)

filtered_df = df[(df["hours"] >= min_hours) & (df["attendance"] >= min_att)]

# =========================
# TITLE
# =========================
st.title("Student Performance AI Dashboard")

# =========================
# ROW 1: DATA + STATS
# =========================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Dataset Preview")
    st.dataframe(filtered_df, use_container_width=True)

with col2:
    st.subheader("Statistics")
    st.write(filtered_df.describe())

# =========================
# ROW 2: GRAPHS
# =========================
st.subheader("Data Visualizations")

col3, col4, col5 = st.columns(3)

with col3:
    fig1, ax1 = plt.subplots()
    ax1.hist(filtered_df["marks"])
    ax1.set_title("Marks Distribution")
    st.pyplot(fig1, use_container_width=True)

with col4:
    fig2, ax2 = plt.subplots()
    ax2.scatter(filtered_df["hours"], filtered_df["marks"])
    ax2.set_title("Hours vs Marks")
    st.pyplot(fig2, use_container_width=True)

with col5:
    fig3, ax3 = plt.subplots()
    ax3.scatter(filtered_df["attendance"], filtered_df["marks"])
    ax3.set_title("Attendance vs Marks")
    st.pyplot(fig3, use_container_width=True)

# =========================
# ROW 3: HEATMAP + INSIGHTS
# =========================
st.subheader("Advanced Analysis")

col6, col7 = st.columns(2)

with col6:
    fig4, ax4 = plt.subplots()
    sns.heatmap(filtered_df.corr(), annot=True, ax=ax4)
    ax4.set_title("Correlation Heatmap")
    st.pyplot(fig4, use_container_width=True)

with col7:
    st.subheader("Key Insights")

    avg_marks = filtered_df["marks"].mean()
    high = filtered_df[filtered_df["hours"] >= 3]["marks"].mean()
    low = filtered_df[filtered_df["hours"] < 3]["marks"].mean()

    st.write("Average Marks:", round(avg_marks, 2))
    st.write("Study Impact:", round(high - low, 2))

# =========================
# ML MODEL (TRAIN)
# =========================
X = df[["hours", "attendance"]]
y = df["marks"]

model = LinearRegression()
model.fit(X, y)

# =========================
# PREDICTION PANEL
# =========================
st.subheader("Predict Student Marks")

col8, col9 = st.columns(2)

with col8:
    input_hours = st.number_input("Study Hours", 0.0, 10.0, 2.0)
    input_att = st.number_input("Attendance (%)", 0.0, 100.0, 70.0)

with col9:
    if st.button("Predict"):
        prediction = model.predict([[input_hours, input_att]])
        st.success(f"Predicted Marks: {round(prediction[0], 2)}")

# =========================
# EXPORT BUTTON
# =========================
st.subheader("⬇ Export Data")

csv = filtered_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name='filtered_students.csv',
    mime='text/csv'
)