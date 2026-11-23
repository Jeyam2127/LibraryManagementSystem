books = [
    {"name": "Python Crash Course", "author": "Jams", "price": 550},
    {"name": "Intoduction of java", "author": "Robert", "price": 700},
    {"name": "Programing in C", "author": "son heung min", "price": 400},
]

def display_books():
    print("\n--- Library Book Details ---")
    print(f"{'Book Name':<25}{'Author':<25}{'Price':<10}")
    print("-" * 60)
    for b in books:
        print(f"{b['name']:<25}{b['author']:<25}{b['price']:<10}")

display_books()