
import darkWhiteMode from './../assets/dark_white_mode.svg';
import {useState, useEffect} from 'react';


const Dashboard = () => {
    
    const [darkMode, setDarkMode] = useState(() => {
      const savedMode = localStorage.getItem('isDarkMode')

      return savedMode ? JSON.parse(savedMode) : false;
    })
    

    const handleDarkMode = () => {
        setDarkMode(prevDarkMode => {
            const newDarkMode = !prevDarkMode;
            document.documentElement.classList.toggle('dark', newDarkMode);
            localStorage.setItem('isDarkMode', JSON.stringify(newDarkMode))
            return newDarkMode;
        });
    };

    useEffect(() => {
        // Apply dark mode class based on state
        document.documentElement.classList.toggle('dark', darkMode);
    }, [darkMode]);

    return (
    <div className={`min-h-screen ${darkMode ? 'dark' : ''}`}>
      {/* Header */}
      <header className='pt-4'>
                <button 
                    onClick={handleDarkMode} 
                    className='p-2 rounded-full transition-transform transform hover:scale-105 hover: dark:fill-white'>
                    <img 
                        src={darkWhiteMode} 
                        alt="Dark and White Mode" 
                        className={`w-12 h-12 ${darkMode ? 'filter invert' : ''}`} 
                        style={{ filter: darkMode ? 'invert(1)' : 'none', transition: 'filter 0.3s' }} />
                </button>
        </header>

      {/* Main Content */}
      <main className="flex-grow p-4">
        {/* Search Bar */}
        <div className="flex justify-center mb-8">
          <input
            type="text"
            placeholder="Search documents"
            className="w-full max-w-lg p-2 rounded border dark:bg-gray-700 dark:text-white focus:outline-none"
          />
        </div>

        {/* Visualization */}
        <div className="h-64 bg-gray-200 dark:bg-gray-700 rounded-lg mb-8">
          {/* Placeholder for data visualization */}
        </div>

        {/* Results Section */}
        <div className="grid gap-4">
          {/* Placeholder for search results */}
        </div>
      </main>
    </div>
  );
};

export default Dashboard;
