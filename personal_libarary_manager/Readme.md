# Personal Library Manager

A simple command-line tool to manage a personal library. This tool allows you to add, update, remove, preview, and search for books using JSON as a data store.

## Features
- 📚 **Add a Book**: Add a new book to the library.
- 📝 **Update Book Details**: Modify the name, content, or author of an existing book.
- ❌ **Remove a Book**: Delete a book from the library.
- 🔍 **Search for a Book**: Find a book by name.
- 📜 **Preview All Books**: List all books in the library.

## Installation
Ensure you have Python and UV installed, then install `Click` (if not already installed):
```sh
pip install click 
```
or
```sh
uv add click
```

## Usage
Run the CLI using:
```sh
python main.py [command] [arguments]
```

### Commands

#### 1️⃣ Add a Book
```sh
python main.py add-book "Book Name" "Content of the Book" "Author Name"
```
Example:
```sh
python main.py add-book "Python Basics" "Introduction to Python" "John Doe"
```

#### 2️⃣ Update Book Details
```sh
python main.py update-book "Book Name" --new-name "New Name" --new-content "New Content" --new-author "New Author"
```
Example:
```sh
python main.py update-book "Python Basics" --new-content "Updated Introduction to Python"
```

#### 3️⃣ Remove a Book
```sh
python main.py remove-book "Book Name"
```
Example:
```sh
python main.py remove-book "Python Basics"
```

#### 4️⃣ Search for a Book
```sh
python main.py search-book "Book Name"
```
Example:
```sh
python main.py search-book "Python Basics"
```

#### 5️⃣ Preview All Books
```sh
python main.py preview-books
```

## JSON Data Storage
The library stores books in `books_data.json`. If the file doesn't exist, it will be created automatically.

## Contributing
Feel free to suggest new features or report issues!

## License
MIT License. Free to use and modify. 😊

