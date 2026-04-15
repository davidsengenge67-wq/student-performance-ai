import joblib

model = joblib.load('../model/model.pkl')

hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance: "))

prediction = model.predict([[hours, attendance]])

print(f"Predicted Score: {prediction[0]:.2f}")