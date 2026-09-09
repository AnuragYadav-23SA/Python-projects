# Python-project-20

list1 = [101, 102, 103, 104, 105]
list2 = [103, 104, 106, 107, 108]

merged = list(set(list1 + list2))
merged.sort()  # sorting just to keep it neat

print("List 1:", list1)
print("List 2:", list2)
print("Merged (no duplicates):", merged)