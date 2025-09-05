import utils

def guest_menu():
    while True:
        print("\n===== Guest Menu =====")
        print("1. Register")
        print("2. Login")
        print("3. Search Books")
        print("0. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            password = input("Password: ")
            utils.register_member(name, email, password, role="member")
            print("✅ Registered successfully.")
        elif choice == "2":
            email = input("Email: ")
            password = input("Password: ")
            user = utils.login(email, password)
            if user:
                print(f"✅ Welcome, {user['Name']} ({user['Role']})")
                if user["Role"] == "librarian":
                    librarian_menu(user)
                else:
                    member_menu(user)
            else:
                print("❌ Invalid login.")
        elif choice == "3":
            term = input("Enter search term: ")
            books = utils.find_books_by_term(term)
            if books:
                for b in books:
                    print(b)
            else:
                print("No books found.")
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice")

def member_menu(user):
    while True:
        print("\n===== Member Menu =====")
        print("1. Search Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("0. Logout")

        choice = input("Enter choice: ")
        if choice == "1":
            term = input("Enter search term: ")
            books = utils.find_books_by_term(term)
            if books:
                for b in books:
                    print(b)
            else:
                print("No books found.")
        elif choice == "2":
            isbn = input("Enter ISBN to borrow: ")
            if utils.issue_book(isbn, user["MemberID"]):
                print("✅ Book borrowed.")
            else:
                print("❌ Book not available.")
        elif choice == "3":
            loan_id = input("Enter LoanID to return: ")
            if utils.return_book(loan_id):
                print("✅ Book returned.")
            else:
                print("❌ Invalid LoanID.")
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("❌ Invalid choice")

def librarian_menu(user):
    while True:
        print("\n===== Librarian Menu =====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. View Overdue Loans")
        print("0. Logout")

        choice = input("Enter choice: ")
        if choice == "1":
            isbn = input("ISBN: ")
            title = input("Title: ")
            author = input("Author: ")
            copies = int(input("Copies: "))
            utils.add_book(isbn, title, author, copies)
            print("✅ Book added.")
        elif choice == "2":
            name = input("Name: ")
            email = input("Email: ")
            password = input("Password: ")
            utils.register_member(name, email, password, role="member")
            print("✅ Member registered.")
        elif choice == "3":
            overdue = utils.overdue_loans()
            if overdue:
                for l in overdue:
                    print(l)
            else:
                print("No overdue loans.")
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    guest_menu()
