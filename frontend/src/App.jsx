import { Routes, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import Home from '../pages/Home';
import Authors from '../pages/Authors';
import Books from '../pages/Books';
import Dashboard from '../pages/Dashboard';
import Students from '../pages/Students';
import Result from '../pages/Result';
import Library from '../pages/Library';
import Professors from '../pages/Professors';
import Marksheet from '../pages/Marksheet';
import './App.css';

function App() {
  return (
    <>
      <Navigation />
      <main className="main-content">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/students" element={<Students />} />
          <Route path="/professors" element={<Professors />} />
          <Route path="/authors" element={<Authors />} />
          <Route path="/books" element={<Books />} />
          <Route path="/library" element={<Library />} />
          <Route path="/result" element={<Result />} />
          <Route path="/marksheet" element={<Marksheet />} />
        </Routes>
      </main>
    </>
  );
}

export default App;
