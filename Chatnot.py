import easyocr
import cv2
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])  # Specify English language

# Empty dictionary for elements
elements_dict = {
    "H": {"name": "Hydrogen", "atomic_number": 1, "symbol": "H"},
    "He": {"name": "Helium", "atomic_number": 2, "symbol": "He"},
    "Li": {"name": "Lithium", "atomic_number": 3, "symbol": "Li"},
    "Be": {"name": "Beryllium", "atomic_number": 4, "symbol": "Be"},
    "B": {"name": "Boron", "atomic_number": 5, "symbol": "B"},
    "C": {"name": "Carbon", "atomic_number": 6, "symbol": "C"},
    "N": {"name": "Nitrogen", "atomic_number": 7, "symbol": "N"},
    "O": {"name": "Oxygen", "atomic_number": 8, "symbol": "O"},
    "F": {"name": "Fluorine", "atomic_number": 9, "symbol": "F"},
    "Ne": {"name": "Neon", "atomic_number": 10, "symbol": "Ne"},
    "Na": {"name": "Sodium", "atomic_number": 11, "symbol": "Na"},
    "Mg": {"name": "Magnesium", "atomic_number": 12, "symbol": "Mg"},
    "Al": {"name": "Aluminum", "atomic_number": 13, "symbol": "Al"},
    "Si": {"name": "Silicon", "atomic_number": 14, "symbol": "Si"},
    "P": {"name": "Phosphorus", "atomic_number": 15, "symbol": "P"},
    "S": {"name": "Sulfur", "atomic_number": 16, "symbol": "S"},
    "Cl": {"name": "Chlorine", "atomic_number": 17, "symbol": "Cl"},
    "Ar": {"name": "Argon", "atomic_number": 18, "symbol": "Ar"},
    "K": {"name": "Potassium", "atomic_number": 19, "symbol": "K"},
    "Ca": {"name": "Calcium", "atomic_number": 20, "symbol": "Ca"},
    "Sc": {"name": "Scandium", "atomic_number": 21, "symbol": "Sc"},
    "Ti": {"name": "Titanium", "atomic_number": 22, "symbol": "Ti"},
    "V": {"name": "Vanadium", "atomic_number": 23, "symbol": "V"},
    "Cr": {"name": "Chromium", "atomic_number": 24, "symbol": "Cr"},
    "Mn": {"name": "Manganese", "atomic_number": 25, "symbol": "Mn"},
    "Fe": {"name": "Iron", "atomic_number": 26, "symbol": "Fe"},
    "Co": {"name": "Cobalt", "atomic_number": 27, "symbol": "Co"},
    "Ni": {"name": "Nickel", "atomic_number": 28, "symbol": "Ni"},
    "Cu": {"name": "Copper", "atomic_number": 29, "symbol": "Cu"},
    "Zn": {"name": "Zinc", "atomic_number": 30, "symbol": "Zn"},
    "Ga": {"name": "Gallium", "atomic_number": 31, "symbol": "Ga"},
    "Ge": {"name": "Germanium", "atomic_number": 32, "symbol": "Ge"},
    "As": {"name": "Arsenic", "atomic_number": 33, "symbol": "As"},
    "Se": {"name": "Selenium", "atomic_number": 34, "symbol": "Se"},
    "Br": {"name": "Bromine", "atomic_number": 35, "symbol": "Br"},
    "Kr": {"name": "Krypton", "atomic_number": 36, "symbol": "Kr"},
    "Rb": {"name": "Rubidium", "atomic_number": 37, "symbol": "Rb"},
    "Sr": {"name": "Strontium", "atomic_number": 38, "symbol": "Sr"},
    "Y": {"name": "Yttrium", "atomic_number": 39, "symbol": "Y"},
    "Zr": {"name": "Zirconium", "atomic_number": 40, "symbol": "Zr"},
    "Nb": {"name": "Niobium", "atomic_number": 41, "symbol": "Nb"},
    "Mo": {"name": "Molybdenum", "atomic_number": 42, "symbol": "Mo"},
    "Tc": {"name": "Technetium", "atomic_number": 43, "symbol": "Tc"},
    "Ru": {"name": "Ruthenium", "atomic_number": 44, "symbol": "Ru"},
    "Rh": {"name": "Rhodium", "atomic_number": 45, "symbol": "Rh"},
    "Pd": {"name": "Palladium", "atomic_number": 46, "symbol": "Pd"},
    "Ag": {"name": "Silver", "atomic_number": 47, "symbol": "Ag"},
    "Cd": {"name": "Cadmium", "atomic_number": 48, "symbol": "Cd"},
    "In": {"name": "Indium", "atomic_number": 49, "symbol": "In"},
    "Sn": {"name": "Tin", "atomic_number": 50, "symbol": "Sn"},
    "Sb": {"name": "Antimony", "atomic_number": 51, "symbol": "Sb"},
    "Te": {"name": "Tellurium", "atomic_number": 52, "symbol": "Te"},
    "I": {"name": "Iodine", "atomic_number": 53, "symbol": "I"},
    "Xe": {"name": "Xenon", "atomic_number": 54, "symbol": "Xe"},
    "Cs": {"name": "Cesium", "atomic_number": 55, "symbol": "Cs"},
    "Ba": {"name": "Barium", "atomic_number": 56, "symbol": "Ba"},
    "La": {"name": "Lanthanum", "atomic_number": 57, "symbol": "La"},
    "Ce": {"name": "Cerium", "atomic_number": 58, "symbol": "Ce"},
    "Pr": {"name": "Praseodymium", "atomic_number": 59, "symbol": "Pr"},
    "Nd": {"name": "Neodymium", "atomic_number": 60, "symbol": "Nd"},
    "Pm": {"name": "Promethium", "atomic_number": 61, "symbol": "Pm"},
    "Sm": {"name": "Samarium", "atomic_number": 62, "symbol": "Sm"},
    "Eu": {"name": "Europium", "atomic_number": 63, "symbol": "Eu"},
    "Gd": {"name": "Gadolinium", "atomic_number": 64, "symbol": "Gd"},
    "Tb": {"name": "Terbium", "atomic_number": 65, "symbol": "Tb"},
    "Dy": {"name": "Dysprosium", "atomic_number": 66, "symbol": "Dy"},
    "Ho": {"name": "Holmium", "atomic_number": 67, "symbol": "Ho"},
    "Er": {"name": "Erbium", "atomic_number": 68, "symbol": "Er"},
    "Tm": {"name": "Thulium", "atomic_number": 69, "symbol": "Tm"},
    "Yb": {"name": "Ytterbium", "atomic_number": 70, "symbol": "Yb"},
    "Lu": {"name": "Lutetium", "atomic_number": 71, "symbol": "Lu"},
    "Hf": {"name": "Hafnium", "atomic_number": 72, "symbol": "Hf"},
    "Ta": {"name": "Tantalum", "atomic_number": 73, "symbol": "Ta"},
    "W": {"name": "Tungsten", "atomic_number": 74, "symbol": "W"},
    "Re": {"name": "Rhenium", "atomic_number": 75, "symbol": "Re"},
    "Os": {"name": "Osmium", "atomic_number": 76, "symbol": "Os"},
    "Ir": {"name": "Iridium", "atomic_number": 77, "symbol": "Ir"},
    "Pt": {"name": "Platinum", "atomic_number": 78, "symbol": "Pt"},
    "Au": {"name": "Gold", "atomic_number": 79, "symbol": "Au"},
    "Hg": {"name": "Mercury", "atomic_number": 80, "symbol": "Hg"},
    "Tl": {"name": "Thallium", "atomic_number": 81, "symbol": "Tl"},
    "Pb": {"name": "Lead", "atomic_number": 82, "symbol": "Pb"},
    "Bi": {"name": "Bismuth", "atomic_number": 83, "symbol": "Bi"},
    "Po": {"name": "Polonium", "atomic_number": 84, "symbol": "Po"},
    "At": {"name": "Astatine", "atomic_number": 85, "symbol": "At"},
    "Rn": {"name": "Radon", "atomic_number": 86, "symbol": "Rn"},
    "Fr": {"name": "Francium", "atomic_number": 87, "symbol": "Fr"},
    "Ra": {"name": "Radium", "atomic_number": 88, "symbol": "Ra"},
    "Ac": {"name": "Actinium", "atomic_number": 89, "symbol": "Ac"},
    "Th": {"name": "Thorium", "atomic_number": 90, "symbol": "Th"},
    "Pa": {"name": "Protactinium", "atomic_number": 91, "symbol": "Pa"},
    "U": {"name": "Uranium", "atomic_number": 92, "symbol": "U"},
    "Np": {"name": "Neptunium", "atomic_number": 93, "symbol": "Np"},
    "Pu": {"name": "Plutonium", "atomic_number": 94, "symbol": "Pu"},
    "Am": {"name": "Americium", "atomic_number": 95, "symbol": "Am"},
    "Cm": {"name": "Curium", "atomic_number": 96, "symbol": "Cm"},
    "Bk": {"name": "Berkelium", "atomic_number": 97, "symbol": "Bk"},
    "Cf": {"name": "Californium", "atomic_number": 98, "symbol": "Cf"},
    "Es": {"name": "Einsteinium", "atomic_number": 99, "symbol": "Es"},
    "Fm": {"name": "Fermium", "atomic_number": 100, "symbol": "Fm"},
    "Md": {"name": "Mendelevium", "atomic_number": 101, "symbol": "Md"},
    "No": {"name": "Nobelium", "atomic_number": 102, "symbol": "No"},
    "Lr": {"name": "Lawrencium", "atomic_number": 103, "symbol": "Lr"},
    "Rf": {"name": "Rutherfordium", "atomic_number": 104, "symbol": "Rf"},
    "Db": {"name": "Dubnium", "atomic_number": 105, "symbol": "Db"},
    "Sg": {"name": "Seaborgium", "atomic_number": 106, "symbol": "Sg"},
    "Bh": {"name": "Bohrium", "atomic_number": 107, "symbol": "Bh"},
    "Hs": {"name": "Hassium", "atomic_number": 108, "symbol": "Hs"},
    "Mt": {"name": "Meitnerium", "atomic_number": 109, "symbol": "Mt"},
    "Ds": {"name": "Darmstadtium", "atomic_number": 110, "symbol": "Ds"},
    "Rg": {"name": "Roentgenium", "atomic_number": 111, "symbol": "Rg"},
    "Cn": {"name": "Copernicium", "atomic_number": 112, "symbol": "Cn"},
    "Nh": {"name": "Nihonium", "atomic_number": 113, "symbol": "Nh"},
    "Fl": {"name": "Flerovium", "atomic_number": 114, "symbol": "Fl"},
    "Mc": {"name": "Moscovium", "atomic_number": 115, "symbol": "Mc"},
    "Lv": {"name": "Livermorium", "atomic_number": 116, "symbol": "Lv"},
    "Ts": {"name": "Tennessine", "atomic_number": 117, "symbol": "Ts"},
    "Og": {"name": "Oganesson", "atomic_number": 118, "symbol": "Og"},
}

def capture_image_from_webcam(image_path):
    """Opens webcam, waits for user to press 'q', and captures an image."""
    cap = cv2.VideoCapture(0)  # Open default webcam

    if not cap.isOpened():
        raise RuntimeError("Could not open webcam.")

    print("Press 'q' to capture the image.")

    while True:
        ret, frame = cap.read()  # Read frame from webcam
        if not ret:
            print("Failed to capture frame.")
            break

        cv2.imshow("Press 'q' to Capture", frame)  # Show the live video feed

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # Capture the image when 'q' is pressed
            cv2.imwrite(image_path, frame)  # Save the captured image
            print(f"Image captured and saved to {image_path}")
            break

    cap.release()
    cv2.destroyAllWindows()  # Close the webcam window
    return image_path

def extract_text_from_image(image_path):
    """Extracts text from an image using EasyOCR."""
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")

        # Read image with OpenCV
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Could not load image at {image_path}. Check path and file integrity.")

        # Convert to grayscale for better OCR results
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Use EasyOCR to extract text
        extracted_texts = reader.readtext(gray_image, detail=0)  # `detail=0` returns just the text

        if not extracted_texts:
            return "No text detected in the image."

        return " ".join(extracted_texts).strip()  # Combine all detected text
    except Exception as e:
        raise RuntimeError(f"Error during OCR processing: {e}") from e

def chat_with_gemini(prompt):
    """Chats with the Gemini AI model, handling API key and errors."""
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not found. Set it using a .env file or system settings.")

    try:
        # Configure Gemini API with the key
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('models/gemini-1.5-pro-latest')  # Best model
        response = model.generate_content(prompt)  # Request the response from Gemini AI
        return response.text.strip()  # Return the AI response without extra spaces
    except Exception as e:
        raise RuntimeError(f"Error communicating with Gemini API: {e}") from e

def get_element_details(image_path):
    """Extracts element symbol from an image and gets details from Gemini AI."""
    # Extract text (element symbol) from the image using OCR
    element_symbol = extract_text_from_image(image_path)

    if not element_symbol:
        return "No element symbol detected in the image."

    print(f"Detected Element Symbol: {element_symbol}")  # Debugging output

    # Clean up and process extracted symbol (e.g., remove extra spaces, ensure uppercase)
    element_symbol = element_symbol.strip().upper()

    # Check if the extracted symbol matches known elements
    if element_symbol in elements_dict:
        # Construct a prompt for the Gemini AI
        element_info = elements_dict[element_symbol]
        prompt = f"Please provide detailed information about the element: {element_info['name']}"
        try:
            # Get the detailed response from Gemini AI
            response = chat_with_gemini(prompt)
            return response
        except Exception as e:
            return f"Error while getting data from Gemini: {e}"
    else:
        return f"Element symbol '{element_symbol}' not found in the dictionary."

# Main execution block
if __name__ == "__main__":
    image_path = "captured_image.jpg"  # Default image path

    try:
        # Open webcam and wait for user to press 'q' to capture the image
        capture_image_from_webcam(image_path)

        # Get element details from the captured image
        response = get_element_details(image_path)
        print(response)  # Print the response from Gemini AI
    except Exception as e:
        print(f"Error: {e}")  # Handle any errors gracefully