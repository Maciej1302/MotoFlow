import React, { useEffect, useState } from 'react';

function App() {
    const [data, setData] = useState(null); // Stan do przechowywania danych
    const [error, setError] = useState(null); // Stan do przechowywania błędów

    useEffect(() => {
        fetch('http://localhost:8000/myapp/')  // Użyj poprawnego endpointu
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response wsas not ok');
                }
                return response.json();
            })
            .then(data => {
                setData(data); // Ustaw dane
            })
            .catch(error => {
                setError(error); // Ustaw błąd
                console.error('Error fetching data:', error); // Wyświetl błąd w konsoli
            });
    }, []);

    return (
        <div>
            <h1>Response from Django</h1>
            {error && <p style={{ color: 'red' }}>Error: {error.message}</p>}
            {data ? (
                <pre>{JSON.stringify(data, null, 2)}</pre> // Wyświetlanie danych
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
}

export default App;  // Eksport komponentu App
