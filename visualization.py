import matplotlib.pyplot as plt

names = ["saniya", "Dipak", "raj", "Dishant"]

marks = [92, 95, 78, 65]

plt.bar(names, marks)

plt.title("Student Marks")

plt.xlabel("Student")

plt.ylabel("Marks")

plt.ylim(0, 100)

plt.show()

highest = max(marks)

index = marks.index(highest)

print("Highest Marks:", highest)

print("Top Student:", names[index])