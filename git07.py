# A school wants to calculate grades for students based on marks obtained fin 5 subjects

marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)

average = sum(marks) / 5

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F (Fail)"

print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
