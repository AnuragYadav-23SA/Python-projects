# Python-project-15
#Character Occurance

text = input("Enter a string: ")

char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("\nCharacter occurrences:")
for char, count in char_count.items():
    print(f"'{char}' → {count}")