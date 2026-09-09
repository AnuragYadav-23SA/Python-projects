# Python-project-17

inventory = ["The Alchemist", "Atomic Habits", "Clean Code", "Rich Dad Poor Dad", "Harry Potter", "Deep Work"]

book = input("Enter book name to search: ")

if book in inventory:
    print(f"'{book}' is available in the inventory!")
else:
    print(f"Sorry, '{book}' is not found in the inventory.")