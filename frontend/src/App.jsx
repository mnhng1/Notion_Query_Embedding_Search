
import './App.css'


import LandingPage from "./components/LandingPage";
import Dashboard from './components/Dashboard';
import PrivateRoutes from './components/ProtectedRoute';

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AuthProvider } from './components/AuthContext';

const App = () => {
  return (
    <AuthProvider>
    <Router>
      <Routes>
        <Route path = "/" element = {<LandingPage/>}></Route>
        <Route element={<PrivateRoutes/>}>
          <Route path = "/dashboard" element = {<Dashboard/>}></Route>
        </Route>
      </Routes>
    </Router>
    </AuthProvider>
  );
};

export default App;


