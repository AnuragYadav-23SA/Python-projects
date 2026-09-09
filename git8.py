# Login Attempt System (max 3 tries)

correct_username = "admin"
correct_password = "pass123"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful! Welcome,", username)
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect credentials. {remaining} attempt(s) left.")
        else:
            print("Too many failed attempts. Account locked.")