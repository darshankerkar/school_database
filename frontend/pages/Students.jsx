import './PageTemplate.css';

export default function Students() {
  const sampleColumns = ['Name', 'Email', 'Roll No', 'Department', 'Actions'];

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>🎓 Students</h1>
        <p>Manage student records</p>
      </div>

      <div className="card">
        <div className="card-header">
          <h2>Student List</h2>
          <button className="btn btn-primary">+ Add Student</button>
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