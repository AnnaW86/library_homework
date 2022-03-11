from turtle import title


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
            print(f'{book["title"]} by {book["author"]}.')
        

    if option == "2":
        print("Searching for a book by title...")
        # TODO - Search for a book by title
        target_book = input("What is the title of the book you're looking for? ")
        target_book_status = False
        for book in library["books"]:
            if target_book.lower() in book["title"].lower():
                print(f'Yes, we have {book["title"]}.')
                target_book_status = True
        if target_book_status == False:
            print("Sorry, we don't seem to have that.")

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

    if option == "4":
        print("Removing a book...")
        # TODO - Remove a book
        title_to_remove = input("What is the title of the book you would like to remove? ")
        for book in library["books"]:
            if title_to_remove.lower() in book["title"].lower():
                library["books"].remove(book)
        

    if option == "5":
        print("Updating a book...")
        # TODO - Update a book
