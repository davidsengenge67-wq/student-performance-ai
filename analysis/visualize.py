import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("../data/student_data.csv")

print("Dataset shape:", df.shape)
print("Columns:", df.columns)

# -------------------------
# 1. Marks distribution
# -------------------------
plt.figure()
plt.hist(df["marks"])
plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Count")
plt.show()

# -------------------------
# 2. Study hours vs marks
# -------------------------
plt.figure()
plt.scatter(df["hours"], df["marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()

# -------------------------
# 3. Attendance vs marks
# -------------------------
plt.figure()
plt.scatter(df["attendance"], df["marks"])
plt.title("Attendance vs Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.show()

# -------------------------
# 4. Correlation heatmap
# -------------------------
plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("Feature Correlation Heatmap")
plt.show()