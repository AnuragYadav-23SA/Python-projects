# Python-project-9
#Menu System

menu = {
    1: ("Burger", 120),
    2: ("Pizza", 250),
    3: ("Pasta", 180),
    4: ("Cold Drink", 60),
    0: ("Exit", 0)
}

while True:
    print("\n--- Welcome to FoodApp ---")
    for key, (item, price) in menu.items():
        if key == 0:
            print(f"{key}. Exit")
        else:
            print(f"{key}. {item} - ₹{price}")

    choice = int(input("\nSelect an option: "))

    if choice == 0:
        print("Thanks for visiting. Goodbye!")
        break
    elif choice in menu:
        print(f"You selected {menu[choice][0]}. Enjoy your meal!")
    else:
        print("Invalid choice, try again.")