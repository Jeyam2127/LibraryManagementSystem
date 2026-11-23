books = [
    {"name": "Python Crash Course", "author": "Eric Matthes", "price": 550, "issued": False},
    {"name": "Introduction of java", "author": "Robert C. Martin", "price": 700, "issued": False},
    {"name": "Programming in C", "author": "Yashavant Kanetkar", "price": 400, "issued": False},
]

def display_books():
    print("\n--- Library Book Details ---")
    print(f"{'Book Name':<25}{'Author':<25}{'Price':<10}{'Status'}")
    print("-" * 70)
    for b in books:
        status = "Issued" if b["issued"] else "Available"
        print(f"{b['name']:<25}{b['author']:<25}{b['price']:<10}{status}")

def issue_book():
    name = input("Enter the book name to issue: ")
    for b in books:
        if b["name"].lower() == name.lower():
            if b["issued"]:
                print("Sorry, this book is already issued.")
            else:
                b["issued"] = True
                print(f"'{b['name']}' has been issued successfully.")
            return
    print("Book not found.")

def main():
    while True:
        print("\n1. Display Books\n2. Issue Book\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_books()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()