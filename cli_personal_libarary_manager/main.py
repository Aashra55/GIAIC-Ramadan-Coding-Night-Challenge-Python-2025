import click
import json     
import os
    
LIBRARY = "books_data.json"  # File to store book data

def load_books():
    """Loads books from the JSON file. If the file does not exist, returns an empty list."""
    if not os.path.exists(LIBRARY):
        print("Library does not exists!")
        return []
    with open(LIBRARY, "r") as file :
        return json.load(file)
    
def save_book(book):
    """Saves the book list to the JSON file."""
    with open(LIBRARY,"w") as file:
        json.dump(book, file, indent=4)

@click.group()
def cli():
    """CLI group for organizing commands."""
    pass

@click.command()
@click.argument("name")
@click.argument("content")
@click.argument("author")
def add_book(name, content, author):
    """Adds a new book to the library."""
    books = load_books()
    
    for book in books:
        if book["name"].lower() == name.lower():  # Case-insensitive check
            click.echo(f"Error: A book with the name '{name}' already exists in the library.")
            return  # Stop execution

    books.append({"name":name, "content":content, "author":author})
    save_book(books)
    click.echo(f"Book '{name}' added in LIBRARY succesfully!")

@click.command()
def preview_books():
    """Displays all books in the library."""
    books = load_books()
    if not books :
        click.echo("No book found in LIBRARY!")
        return 
    for index, book in enumerate(books, 1):
        click.echo(f"{index}. {book['name']}[{book['author']}] '{book['content']}'")
        
@click.command()
@click.argument('name')
def remove_book(name):
    """Removes a book from the library by name."""
    books = load_books()
    updated_books = [book for book in books if book['name'].lower() != name.lower()]
    
    if len(updated_books) == len(books):
        click.echo(f"Book '{name}' not found in LIBRARY!")
    else: 
        save_book(updated_books)
        click.echo(f"Book '{name}' removed from LIBRARY successfully!")

@click.command()
@click.argument('name')
@click.option('--new-name',default=None, help="New name of the book")
@click.option('--new-content',default=None, help="New content of the book")
@click.option('--new-author',default=None, help="New author of the book")
def update_book(name, new_name, new_content, new_author):
    """Update the details of an existing book."""
    books = load_books()
    
    for book in books:
        if book["name"].lower() == name.lower():
            if new_name:
                book["name"] = new_name
            if new_content:
                book["content"] = new_content
            if new_author:
                book["author"] = new_author
            save_book(books)
            click.echo(f"Book '{name}' updated successfully!")
            return
    click.echo(f"Book '{name}' not found in LIBRARY!")    

@click.command()
@click.argument('name')
def search_book(name):
    """Searches for a book by name and displays its details."""
    books = load_books()
    for book in books:
        if book['name'].lower() == name.lower():
            click.echo(f"\n📖 Book Found! \n- Name: {book['name']} \n- Author: {book['author']} \n- Content: {book['content']}\n")
            return
    click.echo(f"Book '{name}' not found in LIBRARY!")

# Registering commands to CLI
cli.add_command(add_book)
cli.add_command(preview_books)
cli.add_command(remove_book)
cli.add_command(update_book)
cli.add_command(search_book)

if __name__ == "__main__":
    cli()
    
    
    
    