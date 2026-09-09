# Python-project-12
#Average Marks

marks = []
n = int(input("How many students? "))

for i in range(n):
    m = float(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

average = sum(marks) / len(marks)

print("Marks:", marks)
print(f"Average marks: {average:.2f}")