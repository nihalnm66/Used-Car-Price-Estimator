# Used Car Price Prediction Web App

A web application that predicts the price of a used car based on its features.  
Built using **Flask**, **Machine Learning (RandomForest Regression)**, and a simple UI with **HTML/CSS/JavaScript**.

## 🚀 Features
- Real-time car price prediction using a trained RandomForest model
- Flask backend with JSON-based API endpoints
- Complete ML pipeline including preprocessing, feature engineering, and model evaluation
- Clean frontend with brand logos and interactive UI animations
- Easy-to-use web interface for entering car details

## 🧠 Machine Learning Model
The ML model is built using:
- RandomForest Regression  
- Feature engineering  
- Data cleaning and preprocessing  
- Model evaluation (R², MAE, etc.)

The trained model is loaded into the Flask backend using `pickle` for fast inference.

## 📁 Project Structure
project/
│── app.py # Main Flask app
│── car_price_app.py # ML pipeline and model code
│── static/ # CSS, JS, logos, UI assets
│── templates/ # HTML files
│── CarPriceProject/ # Dataset files (if small)
│── README.md # Project documentation
│── requirements.txt # Dependencies

## 🔧 Setup & Installation

1. Clone the repository:
git clone https://github.com/<your-username>/Used-Car-Price-Predictor.git
cd Used-Car-Price-Predictor

2. Install dependencies:
pip install -r requirements.txt

3. Run the Flask app:
python app.py

4. Open in browser:
http://127.0.0.1:5000/

## 🎨 UI & Frontend
- HTML/CSS for layout  
- JavaScript for UI interactions  
- GSAP/WebGL animations (optional)  
- Brand logos stored in `static/logos/`

## 📦 Model File
If your model file is large, upload it to Google Drive and include this note:

Download model file: [Click Here](https://drive.google.com/file/d/1PTRp-q1d5Ey5jSgsLagsqKecyFjXFS2Q/view?usp=sharing)
Place it inside the project root before running the Flask app.

## 📜 License
Open-source project. Free to use and modify.
