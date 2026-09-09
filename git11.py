# Python-project-11
# Each book is (name, days_borrowed) — overdue if more than 14 days

books = [
    ("The Alchemist", 20),
    ("Harry Potter", 10),
    ("Clean Code", 17),
    ("Atomic Habits", 5),
    ("Rich Dad Poor Dad", 15),
]

overdue_count = 0

for book, days in books:
    if days > 14:
        overdue_count += 1
        print(f"'{book}' is overdue by {days - 14} day(s).")

print(f"\nTotal overdue books: {overdue_count}")