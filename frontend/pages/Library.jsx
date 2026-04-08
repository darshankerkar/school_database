import './PageTemplate.css';

export default function Library() {
  const sampleColumns = ['Book Title', 'ISBN', 'Category', 'Available', 'Actions'];

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>📘 Library</h1>
        <p>Browse library catalog</p>
      </div>

      <div className="card">
        <div className="card-header">
          <h2>Library Catalog</h2>
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