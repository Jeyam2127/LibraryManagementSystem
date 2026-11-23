# Library Management System

A simple command-line Library Management System written in **Python 3**, built as a Git and GitHub version-control assignment.

**Author:** V Jeyamurugan
**Team:** 9 (Consistency Minders)

## Features

- Display all books with their name, author and price in a table
- Issue a book by name
- Prevents issuing a book that is already issued
- Simple menu: Display Books, Issue Book, Exit

## Project Structure

```
LibraryManagementSystem/
├── library.py    # Main program
└── README.md     # Project documentation
```

## Requirements

- Python 3.x

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Jeyam2127/LibraryManagementSystem.git
   cd LibraryManagementSystem
   ```

2. Run the program:

   ```bash
   python library.py
   ```

## Sample Menu

```
1. Display Books
2. Issue Book
3. Exit
Enter your choice:
```

## Git Workflow Used

| Branch       | Purpose                                   |
|--------------|-------------------------------------------|
| `main`       | Stable version of the project             |
| `book-issue` | Development of the book issue feature     |

Commands practised in this project: `git init`, `git status`, `git add`, `git commit`, `git remote add`, `git push`, `git log`, `git checkout -b`, `git clone`, `git pull`.

## Future Improvements

- Return book feature
- Add new books and remove books
- Save book data to a file or database
- Search books by author

## License

This project is for educational purposes.
