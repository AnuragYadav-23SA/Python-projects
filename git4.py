# A bank wants to calculate simple interest for customers based on principal. rate and tome entered by user.

principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time (in years): "))

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print(f"Simple Interest: ₹{simple_interest:.2f}")
print(f"Total Amount: ₹{total_amount:.2f}")