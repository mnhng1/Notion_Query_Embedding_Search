import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import SearchForm from './components/SearchForm'
import LandingPage from "./components/LandingPage";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path = "/" element = {<LandingPage/>}></Route>
        <Route path = "/search" elemnt = {<SearchForm/>}></Route>
      </Routes>
    </Router>
  );
};

export default App;


