import pandas as pd

df = pd.read_csv("../data/student_data.csv")

print("\n--- KEY INSIGHTS ---")

print("Average marks:", df["marks"].mean())

# High vs low study hours impact
high = df[df["hours"] >= 3]["marks"].mean()
low = df[df["hours"] < 3]["marks"].mean()

print("Avg marks (high study hours):", high)
print("Avg marks (low study hours):", low)

print("Improvement impact:", high - low)

# Attendance impact
high_att = df[df["attendance"] >= 70]["marks"].mean()
low_att = df[df["attendance"] < 70]["marks"].mean()

print("Attendance impact difference:", high_att - low_att)