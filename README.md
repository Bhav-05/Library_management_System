# Library Management System (CLI - CSV)

A lightweight, command-line Library Management System built in Python using CSV files as storage. Supports librarian and member roles, secure login with password hashing (bcrypt), and full book borrowing/returning workflows.

---

##  Features

- **Secure authentication**: hashed passwords using `bcrypt`, role-based access (librarian vs. member).
- **Librarian capabilities**:
  - Add new books
  - View overdue loans
  - Register members
- **Member capabilities**:
  - Search catalog
  - Borrow books
  - Return books
- **Offline storage**: Fully persists data using CSV files (`books.csv`, `members.csv`, `loans.csv`)—no database required.

---

##  Repo Structure

Library_management_System/
├── auth.py # Password hashing & login logic
├── db.py # CSV-based data storage helpers
├── utils.py # Core business logic (members, books, loans)
├── main.py # Menu-driven CLI interface
├── members.csv # Member accounts (librarian + member)
├── books.csv # Sample books catalog
├── loans.csv # Loan records
├── requirements.txt
└── README.md 


##  Setup & Run

### Prerequisites

- Python 3.8+  
- `git` (for cloning)
- [Optional] `venv` for isolated environment

### Instructions

1. Clone the repo:

   ```bash
   git clone https://github.com/Bhav-05/Library_management_System.git
   cd Library_management_System
(Recommended) Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows


2. Install dependencies:

pip install -r requirements.txt


3. Run the CLI app:

python main.py


4. Login with demo accounts:

Librarian
Email: admin@example.com
Password: admin123

Member
Email: bob@example.com
Password: bob123
