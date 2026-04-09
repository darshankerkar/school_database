import './PageTemplate.css';

export default function Marksheet() {
  const sampleColumns = ['Student', 'Subject', 'Marks Obtained', 'Total Marks', 'Percentage'];

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>📋 Marksheet</h1>
        <p>View student marksheets</p>
      </div>

      <div className="card">
        <div className="card-header">
          <h2>Student Marksheets</h2>
          <button className="btn btn-primary">+ Upload Marksheet</button>
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