import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv('../data/student_data.csv')

# Features and target
X = data[['hours', 'attendance']]
y = data['marks']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'model.pkl')

print(" Model trained and saved!")