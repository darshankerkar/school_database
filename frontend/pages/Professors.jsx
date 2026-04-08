import './PageTemplate.css';

export default function Professors() {
  const sampleColumns = ['Name', 'Email', 'Degree', 'Subjects', 'Actions'];

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>👨‍🏫 Professors</h1>
        <p>View and manage professors</p>
      </div>

      <div className="card">
        <div className="card-header">
          <h2>Professor List</h2>
          <button className="btn btn-primary">+ Add Professor</button>
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