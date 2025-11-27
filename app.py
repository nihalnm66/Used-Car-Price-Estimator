from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import datetime

app = Flask(__name__)

# Load trained model once
model = pickle.load(open('car_price_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        brand = request.form['brand']
        model_name = request.form.get('model', '').strip()
        year = int(request.form['year'])
        km_driven = int(request.form['km_driven'])
        fuel = request.form['fuel']
        transmission = request.form['transmission']
        owner = int(request.form['owner'])
        buying_price = request.form.get('buying_price', '').strip()

        # keep form state
        form_data = {
            'brand': brand,
            'model': model_name,
            'year': year,
            'km_driven': km_driven,
            'fuel': fuel,
            'transmission': transmission,
            'owner': owner,
            'buying_price': buying_price
        }

        current_year = datetime.datetime.now().year
        car_age = current_year - year

        premium = ['BMW', 'Audi', 'Mercedes-Benz', 'Jaguar']
        avg_engine = 2000 if brand in premium else 1500
        avg_power  = 180  if brand in premium else 100

        if brand != "Others":
            # Build X exactly like training features
            X = pd.DataFrame(np.zeros((1, len(model.feature_names_in_))), columns=model.feature_names_in_)
            X['km_driven']     = km_driven
            X['owner']         = owner
            X['car_age']       = car_age
            X['engine']        = avg_engine
            X['max_power']     = avg_power

            if f'fuel_{fuel}' in X.columns:
                X[f'fuel_{fuel}'] = 1
            if 'transmission_Manual' in X.columns:
                X['transmission_Manual'] = 1 if transmission == "Manual" else 0
            if f'brand_{brand}' in X.columns:
                X[f'brand_{brand}'] = 1

            price = round(model.predict(X)[0])
            msg = f"Estimated Price for your {brand} {model_name}: ₹{price:,.0f}"
        else:
            # Fallback when brand not in training: use buying price
            if buying_price.isdigit() and int(buying_price) > 0:
                retain = 0.75  # tune if you like
                approx = int(int(buying_price) * retain)
                msg = f"Estimated Resale (Others) from buying ₹{int(buying_price):,} ≈ ₹{approx:,}"
            else:
                msg = "Enter a valid Buying Price to estimate resale (Others)."

        return render_template('index.html', prediction_text=msg, form=form_data)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
