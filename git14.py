# Python-project-14

cities = ("Delhi", "Mumbai", "Paris", "Tokyo", "Dubai")

print("Cities visited by the customer:")
for i, city in enumerate(cities, start=1):
    print(f"{i}. {city}")

print(f"\nTotal cities visited: {len(cities)}")