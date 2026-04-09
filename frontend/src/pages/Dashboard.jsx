import './PageTemplate.css';

export default function Dashboard() {
  return (
    <div className="page-container">
      <div className="page-header">
        <h1>📈 Dashboard</h1>
        <p>System overview and analytics</p>
      </div>

      <div className="card">
        <h2>Statistics</h2>
        <div className="stats-grid">
          <div className="stat-box">
            <span className="stat-label">Total Students</span>
            <span className="stat-value">--</span>
          </div>
          <div className="stat-box">
            <span className="stat-label">Total Professors</span>
            <span className="stat-value">--</span>
          </div>
          <div className="stat-box">
            <span className="stat-label">Total Books</span>
            <span className="stat-value">--</span>
          </div>
          <div className="stat-box">
            <span className="stat-label">Total Authors</span>
            <span className="stat-value">--</span>
          </div>
        </div>
      </div>

      <div className="card">
        <p style={{ color: 'var(--text)', margin: 0 }}>Connect to your backend API to display real-time analytics</p>
      </div>
    </div>
  );
}