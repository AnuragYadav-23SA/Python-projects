# Python-project-19

players = []
n = int(input("How many players? "))

for i in range(n):
    name = input(f"Enter player {i+1} name: ")
    players.append(name)

players.sort()

print("\nPlayers in alphabetical order:")
for i, name in enumerate(players, start=1):
    print(f"{i}. {name}")