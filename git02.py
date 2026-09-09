# create a program to check whether a given username and password match predefined credentials.

#predefined credentials
username = "admin"
password = "12345"

#taking input from user
username_input = input("Enter username: ")
password_input = input("Enter password: ")

# checking if they match*
if username_input == username and password_input == password:
    print("Login successful!")
else:
    print("Invalid username or password. Login failed.")
