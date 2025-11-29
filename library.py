from tabulate import tabulate

# In-memory storage (list of dictionaries)
books = []
next_id = 1  # Auto-increment ID

def addbooks():
    global next_id

    book_name = input("Enter Book Name : ")
    author_name = input("Enter Author Name : ")
    book_code = input("Enter Book Code : ")
    total = input("Enter Total Books : ")
    subject = input("Enter Subject of Books : ")

    # Create book record
    book = {
        "pid": next_id,
        "book_name": book_name,
        "author_name": author_name,
        "book_code": book_code,
        "total": total,
        "subject": subject
    }

    books.append(book)
    next_id += 1
    selectbooks()
    print("\nBooks Added Successfully")


def selectbooks():
    if not books:
        print("\nNo Books Found!")
        return

    table = []
    for b in books:
        table.append([b["pid"], b["book_name"], b["author_name"], b["book_code"], b["total"], b["subject"]])

    print("\n" + tabulate(table, headers=["ID", "BOOK NAME", "AUTHOR NAME", "BOOK CODE", "TOTAL", "SUBJECT"]))


def updatebooks():
    pid = int(input("Enter Book ID to Update: "))

    # Find book
    for book in books:
        if book["pid"] == pid:

            print("\n1. Book Name")
            print("2. Author Name")
            print("3. Book Code")
            print("4. Total")
            print("5. Subject")

            option = int(input("\nWhich field you want to update?: "))

            if option == 1:
                book["book_name"] = input("Enter New Book Name: ")
            elif option == 2:
                book["author_name"] = input("Enter New Author Name: ")
            elif option == 3:
                book["book_code"] = input("Enter New Book Code: ")
            elif option == 4:
                book["total"] = input("Enter New Total Books: ")
            elif option == 5:
                book["subject"] = input("Enter New Subject: ")
            else:
                print("Invalid Option")
                return
            selectbooks()
            print("\nUpdate Successfully")
            return

    print("\nBook ID Not Found!")


def deletebooks():
    pid = int(input("Enter Book ID to Delete: "))

    for book in books:
        if book["pid"] == pid:
            books.remove(book)
            selectbooks()
            print("\nBook Deleted Successfully!")
            return

    print("\nBook ID Not Found!")


# MAIN MENU
while True:
    print("\nWelcome to Library - Select your operation from 1 to 5")
    print("\n1. Add Books")
    print("2. Select Books")
    print("3. Update Books")
    print("4. Delete Books")
    print("5. Exit")

    choice = int(input("\nEnter Your Choice: "))

    if choice == 1:
        addbooks()
    elif choice == 2:
        selectbooks()
    elif choice == 3:
        updatebooks()
    elif choice == 4:
        deletebooks()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid Option!")
