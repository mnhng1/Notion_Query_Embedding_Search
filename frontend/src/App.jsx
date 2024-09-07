
import './App.css'

import LandingPage from "./components/LandingPage";
import Dashboard from './components/Dashboard'

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path = "/" element = {<LandingPage/>}></Route>
        
        <Route path = "/dashboard" element = {<Dashboard/>}></Route>
      </Routes>
    </Router>
  );
};

export default App;


