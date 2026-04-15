import pandas as pd

# Load dataset
df = pd.read_csv("../data/student_data.csv")

print("\n--- BASIC INFO ---")
print(df.info())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- STATISTICS ---")
print(df.describe())

print("\n--- SAMPLE DATA ---")
print(df.head())