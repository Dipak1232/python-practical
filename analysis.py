import pandas as pd

data = {
    "Name": ["raj", "disant", "Mana", "Saniya", "Dipak"],
    "Marks": [78, 85, 89, 91, 90]
}

df = pd.DataFrame(data)

df.to_csv("students.csv", index=False)

students = pd.read_csv("students.csv")

average = students["Marks"].mean()

print("Student Records:")
print(students)

print("Class Average:", average) 