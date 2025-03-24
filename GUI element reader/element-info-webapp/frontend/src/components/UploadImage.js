import React, { useState } from 'react';

const UploadImage = () => {
    const [selectedImage, setSelectedImage] = useState(null);
    const [elementInfo, setElementInfo] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleImageUpload = (event) => {
        const file = event.target.files[0];
        if (file) {
            setSelectedImage(URL.createObjectURL(file));
        }
    };

    const handleCaptureImage = async () => {
        // Logic to capture image from webcam can be implemented here
        // For now, we will just simulate an image capture
        alert('Webcam capture functionality is not implemented yet.');
    };

    const handleSubmit = async () => {
        if (!selectedImage) {
            setError('Please upload or capture an image.');
            return;
        }

        setLoading(true);
        setError('');

        const formData = new FormData();
        formData.append('image', selectedImage);

        try {
            const response = await fetch('http://localhost:5000/get-element-info', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error('Failed to fetch element information.');
            }

            const data = await response.json();
            setElementInfo(data.info);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h2>Upload or Capture an Image</h2>
            <input type="file" accept="image/*" onChange={handleImageUpload} />
            <button onClick={handleCaptureImage}>Capture Image from Webcam</button>
            {selectedImage && <img src={selectedImage} alt="Selected" style={{ width: '300px', marginTop: '10px' }} />}
            <button onClick={handleSubmit} disabled={loading}>
                {loading ? 'Loading...' : 'Submit'}
            </button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {elementInfo && <div><h3>Element Information:</h3><p>{elementInfo}</p></div>}
        </div>
    );
};

export default UploadImage;