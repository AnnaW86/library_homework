
library = {
    "name": "CodeClan Library",
    "books": [
        {
            "author": "George RR Martin",
            "title": "A Song of Ice and Fire"
        },
        {
            "author": "J R. R. Tolkien",
            "title": "The Hobbit"
        },
        {
            "author": "Paul Barry",
            "title": "Head-First Python"
        },
        {
            "author": "Allen B. Downey",
            "title": "Think Python: How to Think Like a Computer Scientist"
        },
        {
            "author": "Eric Matthes",
            "title": "Python Crash Course"
        }
    ]
}

def return_to_menu():
    input("Press any key to return to the main menu. ")

# TODO - Print welcome statement including library name

print(f'Welcome to {library["name"]}!')

option = ""
while option != "q":
    print("Options:")
    print("1 - List all books")
    print("2 - Search for a book by title")
    print("3 - Add a book")
    print("4 - Remove a book")
    print("5 - Update a book")
    print("q - Quit")
    option = input("What would you like to do? \n")

    if option == "1":
        print("Listing all books...")
        # TODO - List all books
        for book in library["books"]:
            print(f'\'{book["title"]}\' by {book["author"]}.')
        return_to_menu()
        

    if option == "2":
        print("Searching for a book by title...")
        # TODO - Search for a book by title
        target_book = input("What is the title of the book you're looking for? ")
        target_book_status = False
        for book in library["books"]:
            if target_book.lower() == book["title"].lower():
                print(f'Yes, we have \'{book["title"]}\'.')
                target_book_status = True
        if target_book_status == False:
            print(f"Sorry, we don't seem to have \'{target_book}\'.")
        return_to_menu()

    if option == "3":
        print("Adding a book...")
        # TODO - Add a book
        title_to_add = input("What is the title of the book you would like to add? ")
        author_to_add = input("What is the name of the author? ")
        library["books"].append(
            {
                "author": author_to_add,
                "title": title_to_add
        }
        )
        print(f"You have added \'{title_to_add}\' by {author_to_add} to the library.")
        return_to_menu()

    if option == "4":
        print("Removing a book...")
        # TODO - Remove a book
        book_found_status = False
        books_to_keep = []
        title_to_remove = input("What is the title of the book you would like to remove? ")
        for book in library["books"]:
            if title_to_remove.lower() == book["title"].lower():
                book_found_status = True
            else:
                books_to_keep.append(book)
        library["books"] = books_to_keep
        if book_found_status == False:
            print(f"I'm sorry, I couldn't find \'{title_to_remove}\' in our library.")
        elif book_found_status == True:
            print(f"\'{title_to_remove}\' has been removed from the library.")
        return_to_menu()

    if option == "5":
        print("Updating a book...")
        # TODO - Update a book
        change_made_status = False
        title_to_change = input("What is the title of the book you would like to update? ")
        title_query = input("Would you like to update the title of the book? y/n ")
        if title_query == "y":
            new_title = input("What would you like the new title to be? ")
        author_query = input("Would you like to update the author of the book? y/n ")
        if author_query == "y":
            new_author = input("What would you like the new author to be? ")
        for book in library["books"]:
            if title_to_change.lower() == book["title"].lower():
                if title_query == "y":
                    book["title"] = new_title
                    change_made_status = True
                if author_query == "y":
                    book["author"] = new_author
                    change_made_status = True
        if change_made_status == True:
            print(f"Your changes to \'{title_to_change}\' have been made.")
        elif title_query == "n" and author_query =="n":
            print(f"You haven't given any details of the changes to be made to \'{title_to_change}\'.")
        else:
            print(f"I'm sorry, I couldn't find \'{title_to_change}\' in our library.")
        return_to_menu()