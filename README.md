# e-library-system
Full Stack E-Library System using Django REST Framework and HTML/CSS/JS with PostgreSQL database. Includes JWT authentication, book search, borrowing/returning, and user profile management.
# 📘 E-Library System

A full-stack *digital library management system* that allows users to browse, search, borrow, and return books online. Built with:

- 🔧 *Backend*: Django & Django REST Framework (DRF)
- 🎨 *Frontend*: HTML, CSS, and JavaScript
- 🗃 *Database*: PostgreSQL
- 🔐 *Authentication*: JWT (JSON Web Tokens)

---

## ✅ Features

- 🔐 User registration and login
- 📚 Book search and filter (by title, author, category)
- ✅ Borrow and return books with real-time status updates
- 🧾 View borrowing history and due dates
- ⚠ Notification-ready system for return reminders (future scope)
- 🚀 Optional deployment on Heroku + Netlify

---
## 📂 Project Structure

e-library-system/ ├── backend/              # Django backend │   ├── elibrary/         # Project settings │   ├── books/            # Book app │   ├── manage.py │   └── requirements.txt ├── frontend/             # HTML + CSS + JS │   ├── index.html │   ├── login.html │   ├── profile.html │   ├── book.html │   ├── css/ │   └── js/ ├── database/             # Optional PostgreSQL schema ├── README.md └── assets/               # Screenshots or UI images

---

## 🧰 Tech Stack

| Layer      | Technology                     |
|------------|--------------------------------|
| Frontend   | HTML, CSS, JavaScript          |
| Backend    | Django, Django REST Framework  |
| Auth       | JWT (via DRF SimpleJWT)        |
| Database   | PostgreSQL                     |

---

## 🔧 Setup Instructions

### 🔹 Backend Setup (Django)

```bash
cd backend
python -m venv env
env\Scripts\activate     # Windows
# or
source env/bin/activate  # Mac/Linux

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

🔹 Frontend Setup (HTML/JS)

No build step needed — simply open frontend/index.html in your browser.

> Tip: You can serve it via a simple server like Live Server extension in VS Code.




---
🔐 Authentication (JWT)

1. Login: POST /api/token/ with username & password


2. Save access token to localStorage


3. Use Authorization: Bearer <token> for all API requests




---

🚀 API Endpoints

Method	Endpoint	Description

POST	/api/token/	Get JWT tokens
GET	/api/books/	List all books
POST	/api/borrow/	Borrow a book
POST	/api/return/	Return a book
GET	/api/profile/	Get user borrow history



---

