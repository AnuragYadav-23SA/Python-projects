# Bonus Eligibility Checker

def check_bonus_eligibility(attendance, rating):
    if attendance >= 75 and rating >= 8:
        return "✅ Eligible for Bonus!"
    elif attendance >= 75 and rating < 8:
        return "❌ Not Eligible — Performance rating is too low."
    elif attendance < 75 and rating >= 8:
        return "❌ Not Eligible — Attendance is too low."
    else:
        return "❌ Not Eligible — Both attendance and rating are below the required criteria."

# Taking input from the user
name       = input("Enter employee name: ")
attendance = float(input("Enter attendance percentage (e.g. 85): "))
rating     = float(input("Enter performance rating out of 10 (e.g. 9): "))

# Checking and displaying result
result = check_bonus_eligibility(attendance, rating)
print(f"\nEmployee : {name}")
print(f"Result   : {result}")
