# Python-project-16
#Student Management System

students = {}

while True:
    print("\n1. Add Student")
    print("2. View Student")
    print("3. View All Students")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        students[roll] = {"Name": name, "Marks": marks}
        print(f"Student '{name}' added successfully!")

    elif choice == "2":
        roll = input("Enter Roll Number to search: ")
        if roll in students:
            s = students[roll]
            print(f"Name: {s['Name']}, Marks: {s['Marks']}")
        else:
            print("Student not found!")

    elif choice == "3":
        if students:
            print("\n--- All Students ---")
            for roll, info in students.items():
                print(f"Roll {roll} | {info['Name']} | Marks: {info['Marks']}")
        else:
            print("No records found.")

    elif choice == "4":
        roll = input("Enter Roll Number to delete: ")
        if roll in students:
            print(f"Student '{students[roll]['Name']}' deleted.")
            del students[roll]
        else:
            print("Student not found!")

    elif choice == "5":
        print("Exiting system. Bye!")
        break
    else:
        print("Invalid option, try again.")