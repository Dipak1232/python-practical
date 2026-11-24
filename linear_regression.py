from sklearn.linear_model import LinearRegression
import pandas as pd

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Score": [35, 40, 50, 55, 65, 70, 80, 85]
}

df = pd.DataFrame(data)

X = df[["Hours"]]

y = df["Score"]

model = LinearRegression()

model.fit(X, y)

new_student = pd.DataFrame({"Hours": [4.5]})

predicted_score = model.predict(new_student)

print("Predicted Score:", round(predicted_score[0], 2))