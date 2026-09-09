# A movie theatre wants to assign ticket pricing based on age categories such as child, adult and senior citizens.

age = int(input("Enter age:"))

if age <= 12:
  price = 100
  category = "Child"
elif age <= 60:
  price = 200
  category = "Adult"
else:
  price = 150
  category = "Senior Citizen"

print(f"Category: {category}")
print(f"Price: ₹{price}")