import React, { useState } from 'react';
import UploadImage from './components/UploadImage';

function App() {
    const [elementInfo, setElementInfo] = useState(null);

    const handleElementInfo = (info) => {
        setElementInfo(info);
    };

    return (
        <div className="App">
            <h1>Element Information Finder</h1>
            <UploadImage onElementInfo={handleElementInfo} />
            {elementInfo && (
                <div className="element-info">
                    <h2>Element Information:</h2>
                    <p>{elementInfo}</p>
                </div>
            )}
        </div>
    );
}

export default App;