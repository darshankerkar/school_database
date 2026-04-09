import { Link } from 'react-router-dom';
import './Home.css';

export default function Home() {
  const features = [
    { icon: '🎓', title: 'Students', desc: 'Manage student information', link: '/students' },
    { icon: '👨‍🏫', title: 'Professors', desc: 'View and manage professors', link: '/professors' },
    { icon: '📘', title: 'Library', desc: 'Browse library catalog', link: '/library' },
    { icon: '✍️', title: 'Authors', desc: 'Explore book authors', link: '/authors' },
    { icon: '📚', title: 'Books', desc: 'View all books', link: '/books' },
    { icon: '📊', title: 'Results', desc: 'Check student results', link: '/result' },
    { icon: '📋', title: 'Marksheet', desc: 'View marksheets', link: '/marksheet' },
    { icon: '📈', title: 'Dashboard', desc: 'Analytics overview', link: '/dashboard' },
  ];

  return (
    <div className="home">
      <header className="home-header">
        <h1>School Database</h1>
        <p>Manage students, professors, library, and academic records</p>
      </header>

      <section className="features-grid">
        {features.map((feature) => (
          <Link key={feature.link} to={feature.link} className="feature-card">
            <span className="feature-icon">{feature.icon}</span>
            <h3>{feature.title}</h3>
            <p>{feature.desc}</p>
          </Link>
        ))}
      </section>
    </div>
  );
}
