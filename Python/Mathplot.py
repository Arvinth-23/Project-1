import matplotlib.pyplot as plt
students = ["Arun", "Beena", "Charan", "Divya", "Esha"]
math_marks = [78, 66, 90, 55, 80]
students, math_marks
plt.plot(students, math_marks)
plt.title("Math Marks - Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()plt.bar(students, math_marks)
plt.title("Math Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
plt.plot(students, math_marks, marker='o', linestyle='--')
plt.title("Math Marks with Markers")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()