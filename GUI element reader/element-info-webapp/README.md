# Element Info Web Application

This project is a web application that allows users to upload or capture an image of a chemical element and retrieve detailed information about that element using a backend powered by the Gemini AI model.

## Project Structure

```
element-info-webapp
├── backend
│   ├── Chatnot.py          # Backend logic for image processing and AI interaction
│   ├── requirements.txt     # Python dependencies for the backend
│   └── .env                 # Environment variables, including API keys
├── frontend
│   ├── public
│   │   └── index.html       # Main HTML file for the frontend
│   ├── src
│   │   ├── App.js           # Main React component for the application
│   │   ├── index.js         # Entry point for the React application
│   │   └── components
│   │       └── UploadImage.js # Component for uploading or capturing images
├── package.json              # Configuration file for npm
├── .gitignore                # Files and directories to ignore in Git
└── README.md                 # Documentation for the project
```

## Setup Instructions

### Backend

1. Navigate to the `backend` directory:
   ```
   cd backend
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the `backend` directory and add your `GOOGLE_API_KEY`:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

### Frontend

1. Navigate to the root of the project:
   ```
   cd element-info-webapp
   ```

2. Install the frontend dependencies:
   ```
   npm install
   ```

3. Start the frontend application:
   ```
   npm start
   ```

## Usage

1. Open the web application in your browser.
2. Use the upload feature to select an image or capture an image using your webcam.
3. The application will process the image, identify the chemical element, and display detailed information about it.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.