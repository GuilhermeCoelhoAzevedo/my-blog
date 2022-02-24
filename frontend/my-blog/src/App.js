import './App.css';
import HomePage from './pages/HomePage';
import AboutPage from './pages/AboutPage';
import ArticlePage from './pages/ArticlePage';
import ArticlesListPage from './pages/ArticlesListPage';
import NotFoundPage from './pages/NotFoundPage';
import NavBar from './components/NavBar';
import  { Routes, Route } from "react-router-dom"

function App() {
  return (
    <div className="App">
      <NavBar/>
      <div id="page-body">
        <Routes>
            <Route path="/" element={<HomePage/>}/>
            <Route path="/about" element={<AboutPage/>}/>
            <Route path="/articles-list" element={<ArticlesListPage/>}/>
            <Route path="/article/:name" element={<ArticlePage/>}/>
            <Route path="*" element={<NotFoundPage/>}/>
        </Routes>
      </div>
    </div>
  );
}

export default App;
