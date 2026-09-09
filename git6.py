# write a program to find the largest among three entered sales figures.

sale1 = float(input("Enter first sales figure: "))
sale2 = float(input("Enter second sales figure: "))
sale3 = float(input("Enter third sales figure: "))

largest = max(sale1, sale2, sale3)
print(f"The largest sales figure is: ₹{largest}")