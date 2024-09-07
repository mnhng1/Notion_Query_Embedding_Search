const LandingPage = () => {
    return (
      <div className="min-h-screen flex flex-col justify-between bg-gray-100 text-gray-800 px-4">
        {/* Main content */}
        <div className="flex-grow flex flex-col justify-center items-center">
          <h1 className="text-5xl font-bold mb-8">Welcome to Notion Query Search</h1>
          <p className="text-lg mb-6">
            Search and visualize clusters of semantically related documents.
          </p>
          <button className="bg-blue-500 text-white font-semibold py-2 px-4 rounded-lg hover:bg-blue-600 transition">
            Get Started
          </button>
        </div>
        {/* Footer */}
        <footer className="text-center py-4">
          <p>Copyright © 2024 NQS</p>
        </footer>
      </div>
    );
  };

export default LandingPage;