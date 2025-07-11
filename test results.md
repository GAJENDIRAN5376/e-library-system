# ✅ Test Results – E-Library System

This file contains the test results for both backend API and frontend functionality of the E-Library project.

---

## 🔁 Backend API Testing (Django + DRF + JWT)

| Endpoint             | Method | Auth Required | Status Code | Test Result       | Notes                      |
|----------------------|--------|---------------|-------------|--------------------|----------------------------|
| /api/token/        | POST   | ❌ No         | ✅ 200       | Login success      | Returns access & refresh tokens |
| /api/books/        | GET    | ✅ Yes        | ✅ 200       | Book list loaded   | Returns all books          |
| /api/borrow/       | POST   | ✅ Yes        | ✅ 200       | Book borrowed      | Status changes to unavailable |
| /api/return/       | POST   | ✅ Yes        | ✅ 200       | Book returned      | Marks returned_at date     |
| /api/profile/      | GET    | ✅ Yes        | ✅ 200       | History loaded     | Displays borrowed books     |
| /api/books/invalid/| GET    | ✅ Yes        | ❌ 404       | Not Found          | Tested invalid endpoint     |

---

## 👨‍💻 Manual Frontend Testing (HTML + JS)

| Page           | Result       | Status |
|----------------|--------------|--------|
| login.html   | ✅ Token saved to localStorage | ✅ PASS |
| index.html   | ✅ Book list shows (with status) | ✅ PASS |
| book.html    | ✅ Loads book detail & borrow works | ✅ PASS |
| profile.html | ✅ Shows history with return dates | ✅ PASS |

---

## 🛠 Functional Test Summary

- 🔐 User Authentication: *Working* (JWT tokens issued and validated)
- 📚 Book Borrow/Return: *Working*
- 🧾 History Tracking: *Working*
- ❌ Error Handling: Basic (no alerts for invalid token, expired session)
- ⚠ Edge Cases (e.g., borrowing unavailable book): *Properly blocked*

---

## 🧪 Future Testing Suggestions

- [ ] Add Django unit tests using TestCase
- [ ] Add JavaScript form validations (e.g., empty username)
- [ ] Display better UI messages for failed actions
- [ ] Test expired/invalid tokens handling

---

*Tested By:* Gajendiran K  
*Date:* July 2025  
*Tool Used:* Postman (API), Chrome (Frontend), VS Code
