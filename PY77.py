'''
Write a Python program to manage a small library using a dictionary. The program must repeatedly allow the user to add books, issue books, return books, \
and display the current book record,

Conditions:

-Store book title as the key and available copies as the value.

A book can be issued only if it exists and at least one copy is available.

Return a book only if it already exists in the library record.

Book names should work regardless of uppercase or lowercase letters. 
'''

books = {}

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ").lower()
        copies = int(input("Enter number of copies: "))

        if book in books:
            books[book] = books[book] + copies
        else:
            books[book] = copies

        print("Book added successfully.")

    elif choice == "2":
        book = input("Enter book name: ").lower()

        if book in books and books[book] > 0:
            books[book] = books[book] - 1
            print("Book issued successfully.")
        else:
            print("Book not available.")

    elif choice == "3":
        book = input("Enter book name: ").lower()

        if book in books:
            books[book] = books[book] + 1
            print("Book returned successfully.")
        else:
            print("Book does not exist in the library.")

    elif choice == "4":
        print("\nCurrent Book Record:")

        if len(books) == 0:
            print("Library is empty.")
        else:
            for book in books:
                print(book, ":", books[book], "copies")

    elif choice == "5":
        print("Exiting library...")
        break

    else:
        print("Invalid choice.")