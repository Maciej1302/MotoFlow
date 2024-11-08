import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';  // Import komponentu App

ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root')  // Upewnij się, że element o ID 'root' istnieje w index.html
);
