import React, { useEffect, useState } from "react";

function App() {
  const [books, setBooks] = useState([]);
  const [search, setSearch] = useState("");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  // ✅ FETCH BOOKS (SAFE + NO DUPLICATES)
  useEffect(() => {
    fetchBooks();
  }, []);

  const fetchBooks = async () => {
    try {
      setLoading(true);

      const res = await fetch("http://127.0.0.1:8000/api/books/");
      const data = await res.json();

      console.log("API DATA:", data);

      // ✅ REMOVE DUPLICATES BY TITLE
      const uniqueBooks = [
        ...new Map(data.map((b) => [b.title, b])).values(),
      ];

      setBooks(uniqueBooks);
    } catch (err) {
      console.error("Error fetching books:", err);
    } finally {
      setLoading(false);
    }
  };

  // ✅ FILTER BOOKS
  const filteredBooks = books.filter((book) =>
    book.title?.toLowerCase().includes(search.toLowerCase())
  );

  // ✅ ASK AI (RAG endpoint placeholder)
  const handleAsk = async () => {
    if (!question.trim()) return;

    try {
      const res = await fetch("http://127.0.0.1:8000/api/ask/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question }),
      });

      const data = await res.json();
      setAnswer(data.answer);
    } catch (err) {
      console.error("Ask error:", err);
    }
  };

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>
      <h1>📚 Book AI Platform</h1>

      {/* ================= AI SECTION ================= */}
      <div style={{ marginBottom: 20 }}>
        <h2>Ask AI</h2>

        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask about books..."
          style={{ padding: 8, width: "60%" }}
        />

        <button
          onClick={handleAsk}
          style={{ marginLeft: 10, padding: 8 }}
        >
          Ask
        </button>

        {answer && (
          <div
            style={{
              marginTop: 10,
              padding: 10,
              background: "#f1f1f1",
            }}
          >
            <b>Answer:</b> {answer}
          </div>
        )}
      </div>

      {/* ================= SEARCH ================= */}
      <input
        placeholder="🔍 Search books..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        style={{
          padding: 8,
          width: "60%",
          marginBottom: 20,
        }}
      />

      {/* ================= BOOK LIST ================= */}
      <h2>Books</h2>

      {loading ? (
        <p>Loading books...</p>
      ) : books.length === 0 ? (
        <p>No books found 😢</p>
      ) : filteredBooks.length === 0 ? (
        <p>No matching books 😢</p>
      ) : (
        filteredBooks.map((book) => (
          <div
            key={book.id}
            style={{
              border: "1px solid #ccc",
              margin: 10,
              padding: 10,
              borderRadius: 5,
            }}
          >
            <h3>{book.title}</h3>

            {/* ⚠️ FIX: your backend uses description as price */}
            <p>💰 Price: {book.description}</p>

            <p>⭐ Rating: {book.rating}</p>

            {book.url && (
              <a href={book.url} target="_blank" rel="noreferrer">
                View Source
              </a>
            )}
          </div>
        ))
      )}
    </div>
  );
}

export default App;