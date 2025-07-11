const API = "http://127.0.0.1:8000/api/";
const token = localStorage.getItem("token");

async function fetchBooks() {
  const res = await fetch(API + "books/", {
    headers: { Authorization: Bearer ${token} }
  });

  const books = await res.json();
  const listDiv = document.getElementById("book-list");

  books.forEach(book => {
    const bookDiv = document.createElement("div");
    bookDiv.innerHTML = `
      <h3>${book.title}</h3>
      <p>Author: ${book.author}</p>
      <p>Status: ${book.is_available ? "✅ Available" : "❌ Borrowed"}</p>
    `;
    listDiv.appendChild(bookDiv);
  });
}

if (document.getElementById("book-list")) {
  fetchBooks();
}
