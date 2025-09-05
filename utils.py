import db
import auth
from datetime import datetime, timedelta

BOOKS_FILE = "books.csv"
MEMBERS_FILE = "members.csv"
LOANS_FILE = "loans.csv"

BOOK_FIELDS = ["ISBN", "Title", "Author", "TotalCopies", "AvailableCopies"]
MEMBER_FIELDS = ["MemberID", "Name", "Email", "PasswordHash", "Role"]
LOAN_FIELDS = ["LoanID", "MemberID", "ISBN", "IssueDate", "DueDate", "ReturnDate"]

# -------------------- Members -------------------- #
def register_member(name, email, password, role="member"):
    members = db.read_csv(MEMBERS_FILE, MEMBER_FIELDS)
    member_id = str(len(members) + 1)
    pw_hash = auth.hash_password(password)
    row = {
        "MemberID": member_id,
        "Name": name,
        "Email": email,
        "PasswordHash": pw_hash,
        "Role": role
    }
    db.append_csv(MEMBERS_FILE, MEMBER_FIELDS, row)
    return True

def find_member_by_email(email):
    members = db.read_csv(MEMBERS_FILE, MEMBER_FIELDS)
    for m in members:
        if m["Email"] == email:
            return m
    return None

def login(email, password):
    m = find_member_by_email(email)
    if not m:
        return None
    if auth.check_password(password, m["PasswordHash"]):
        return m
    return None

# -------------------- Books -------------------- #
def add_book(isbn, title, author, copies):
    books = db.read_csv(BOOKS_FILE, BOOK_FIELDS)
    row = {
        "ISBN": isbn,
        "Title": title,
        "Author": author,
        "TotalCopies": str(copies),
        "AvailableCopies": str(copies)
    }
    db.append_csv(BOOKS_FILE, BOOK_FIELDS, row)
    return True

def list_books():
    return db.read_csv(BOOKS_FILE, BOOK_FIELDS)

def find_books_by_term(term):
    books = list_books()
    return [b for b in books if term.lower() in b["Title"].lower() 
            or term.lower() in b["Author"].lower()
            or term.lower() in b["ISBN"].lower()]

# -------------------- Loans -------------------- #
def issue_book(isbn, member_id, days=14):
    books = list_books()
    loans = db.read_csv(LOANS_FILE, LOAN_FIELDS)
    
    for book in books:
        if book["ISBN"] == isbn and int(book["AvailableCopies"]) > 0:
            book["AvailableCopies"] = str(int(book["AvailableCopies"]) - 1)
            db.write_csv(BOOKS_FILE, BOOK_FIELDS, books)
            loan_id = str(len(loans) + 1)
            issue_date = datetime.today().strftime("%Y-%m-%d")
            due_date = (datetime.today() + timedelta(days=days)).strftime("%Y-%m-%d")
            row = {
                "LoanID": loan_id,
                "MemberID": member_id,
                "ISBN": isbn,
                "IssueDate": issue_date,
                "DueDate": due_date,
                "ReturnDate": ""
            }
            db.append_csv(LOANS_FILE, LOAN_FIELDS, row)
            return True
    return False

def return_book(loan_id):
    loans = db.read_csv(LOANS_FILE, LOAN_FIELDS)
    books = list_books()
    for loan in loans:
        if loan["LoanID"] == loan_id and loan["ReturnDate"] == "":
            loan["ReturnDate"] = datetime.today().strftime("%Y-%m-%d")
            for book in books:
                if book["ISBN"] == loan["ISBN"]:
                    book["AvailableCopies"] = str(int(book["AvailableCopies"]) + 1)
            db.write_csv(BOOKS_FILE, BOOK_FIELDS, books)
            db.write_csv(LOANS_FILE, LOAN_FIELDS, loans)
            return True
    return False

def overdue_loans():
    loans = db.read_csv(LOANS_FILE, LOAN_FIELDS)
    today = datetime.today().strftime("%Y-%m-%d")
    return [l for l in loans if l["ReturnDate"] == "" and l["DueDate"] < today]
