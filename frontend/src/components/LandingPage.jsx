import darkWhiteMode from './../assets/dark_white_mode.svg';
import {useState, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from './AuthContext';


const LandingPage = () => {
    const navigate = useNavigate();
    const { isAuthenticated, login } = useAuth();

    const [isDarkMode, setIsDarkMode] = useState(() => {
        // Retrieve the dark mode state from local storage
        const savedMode = localStorage.getItem('isDarkMode');
        return savedMode ? JSON.parse(savedMode) : false;
    });


    

    useEffect(() => {
        if (isDarkMode) {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }

        localStorage.setItem('isDarkMode', JSON.stringify(isDarkMode));
      }, [isDarkMode]);



    const handleBlackMode = () => {
      
        setIsDarkMode(!isDarkMode)
        localStorage.setItem('darkMode', !isDarkMode);
        
    }

    useEffect(() => {
      if (isAuthenticated) {
        navigate('/dashboard')
      }
    }, [isAuthenticated, login, navigate]);
    
    async function handleGetStart() {
      
          // Step 1: Check if user is authenticated by making a backend request
          if (!isAuthenticated) {
            login();
          }
          
          else {
              // Step 3: If authenticated, proceed to dashboard with state
              navigate('/dashboard');
          }
        }
 
    return (
        <div className="min-h-screen flex flex-col justify-between bg-gray-100 dark:bg-gray-900 text-gray-800 dark:text-gray-100 px-4">
        <header className='pt-4'>
                <button 
                    onClick={handleBlackMode} 
                    className='p-2 rounded-full transition-transform transform hover:scale-105 hover: dark:fill-white'>
                    <img 
                        src={darkWhiteMode} 
                        alt="Dark and White Mode" 
                        className={`w-12 h-12 ${isDarkMode ? 'filter invert' : ''}`} 
                        style={{ filter: isDarkMode ? 'invert(1)' : 'none', transition: 'filter 0.3s' }} />
                </button>
        </header>
  
        <div className="flex-grow flex flex-col justify-center items-center">
          <h1 className="text-5xl font-bold mb-8">Welcome to Notion Query Search</h1>
          <p className="text-lg mb-6">
            Search and visualize clusters of semantically related documents.
          </p>
          <button onClick ={handleGetStart}className="bg-blue-500 dark:bg-blue-700 text-white font-semibold py-2 px-4 rounded-lg hover:bg-blue-600 dark:hover:bg-blue-800 transition">
            Get Started With Notion
          </button>
        </div>
  
        <footer className="text-center py-4">
          <p>Copyright © 2024 NQS</p>
        </footer>
      </div>
    );
  };

export default LandingPage;