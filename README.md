# Used Car Price Prediction Web App

A powerful machine learning-based platform designed to accurately predict the resale value of used cars. This application replaces manual price estimation with a data-driven approach, utilizing a RandomForest Regression model to analyze vehicle features and provide instant market valuations.

## 🚀 Features
* **Real-time Price Prediction**: Get instant valuation results based on vehicle specifications.
* **Complete ML Pipeline**: Includes integrated data preprocessing, feature engineering, and model evaluation.
* **Interactive UI**: A clean, modern interface featuring brand logos and smooth animations for an engaging user experience.
* **API Integration**: A Flask-based backend that serves predictions through JSON endpoints.
* **Data-Driven Insights**: Leverages historical car data to provide accurate results.

## 🛠️ Tech Stack
* **Frontend**: HTML5, CSS3, and JavaScript for an interactive and responsive user interface.
* **Backend**: Flask (Python) for handling server logic and API requests.
* **Machine Learning**: RandomForest Regression for high-accuracy price forecasting.
* **Deployment Assets**: `pickle` for model serialization and fast inference.

## 🧠 Machine Learning Pipeline
The core intelligence of the system is built through a rigorous 4-step process:
1. **Data Preprocessing**: Handling missing values, removing outliers, and cleaning the dataset.
2. **Feature Engineering**: Transforming raw vehicle data into meaningful inputs for the regression model.
3. **Model Training**: Utilizing RandomForest Regression to capture complex patterns in car pricing.
4. **Evaluation**: Assessing performance through metrics such as $R^2$ (Coefficient of Determination) and MAE (Mean Absolute Error).

## 📁 Project Structure
```text
project/
│── app.py                # Main Flask application
│── car_price_app.py      # ML pipeline and model logic
│── static/               # CSS, JS, and Brand Logos
│── templates/            # HTML Frontend files
│── CarPriceProject/      # Dataset files
│── requirements.txt      # Project dependencies
└── README.md             # Documentation
```

## 💻 Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/Used-Car-Price-Predictor.git
   cd Used-Car-Price-Predictor
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Model File**: 
   Download the pre-trained model [here](https://drive.google.com/file/d/1PTRp-q1d5Ey5jSgsLagsqKecyFjXFS2Q/view?usp=sharing) and place it in the project root.
4. **Run the Flask app**:
   ```bash
   python app.py
   ```
5. **Access the Web App**:
   Open `http://127.0.0.1:5000/` in your browser.

## 📜 License
Open-source project. Free to use, modify, and distribute for educational and commercial purposes.
