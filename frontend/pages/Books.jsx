import './PageTemplate.css';

export default function Books() {
  const sampleColumns = ['Title', 'Author', 'ISBN', 'Category', 'Actions'];

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>📚 Books</h1>
        <p>View all books in the library</p>
      </div>

      <div className="card">
        <div className="card-header">
          <h2>Book List</h2>
          <button className="btn btn-primary">+ Add Book</button>
        </div>

        <table className="data-table">
          <thead>
            <tr>
              {sampleColumns.map((col) => (
                <th key={col}>{col}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            <tr>
              <td colSpan={sampleColumns.length} style={{ textAlign: 'center', color: 'var(--text)' }}>
                No data yet. Connect to your backend API.
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}