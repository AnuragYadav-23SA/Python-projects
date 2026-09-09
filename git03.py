# A traffic monitoring system needs to determine whether a vehicle exceeded the speed limit.

speed_limit = 60 #km/h
vehicle_speed = float(input("Enter the speed of the vehicle (in km/h): "))

if vehicle_speed > speed_limit:
    print(f"The vehicle is speeding by {vehicle_speed - speed_limit} km/h.")
else:
    print("The vehicle is within the speed limit.")
