import './PageTemplate.css';

export default function Authors() {
  const sampleColumns = ['Name', 'Books', 'Bio', 'Actions'];

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>✍️ Authors</h1>
        <p>Explore book authors</p>
      </div>

      <div className="card">
        <div className="card-header">
          <h2>Author List</h2>
          <button className="btn btn-primary">+ Add Author</button>
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