
import './App.css'


import LandingPage from "./components/LandingPage";
import Dashboard from './components/Dashboard';
import PrivateRoutes from './components/ProtectedRoute';

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path = "/" element = {<LandingPage/>}></Route>
        <Route element={<PrivateRoutes/>}>
          <Route path = "/dashboard" element = {<Dashboard/>}></Route>
        </Route>
      </Routes>
    </Router>
  );
};

export default App;


