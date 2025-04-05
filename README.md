[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://seattle-airbnb-pricemodel-hwfbymaq9c8dppk6kydjhc.streamlit.app)



# 🏠 Airbnb Price Predictor – Seattle

This project is a Streamlit-based interactive app that predicts nightly Airbnb prices in Seattle based on listing features like room type, number of beds, location, amenities, and more.

## 🚀 Features

- Predicts nightly Airbnb prices using a trained XGBoost model
- Interactive UI built with Streamlit
- Feature engineering includes location intelligence and amenities parsing
- One-hot encoded categorical features
- Log-transformed price target for improved performance

## 📁 Project Structure

```
airbnb-price-app/
├── app.py                  # Streamlit app
├── model/
│   ├── airbnb_model.pkl    # Trained XGBoost model
│   └── model_features.pkl  # Feature column names used in training
├── assets/                 # Optional: icons, images, maps
└── requirements.txt        # Python dependencies
```

## ✅ Setup Instructions

### 1. Clone the Repo & Set Up the Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit xgboost scikit-learn pandas numpy matplotlib joblib
```

### 3. Launch the App

> ⚠️ Do **not** use `streamlit run app.py` directly.  
> macOS/Anaconda can override environments and cause import errors with packages like `xgboost`.

Instead, use:

```bash
.venv/bin/python -m streamlit run app.py
```

This ensures the app runs inside the virtual environment and avoids `ModuleNotFoundError`.

## 🧠 Why This Matters

Using `python -m streamlit` guarantees that Streamlit runs with the virtual environment's `site-packages`, not your system or Anaconda environment.

## 📊 Model Overview

- Model: `XGBRegressor`
- Training target: `log(price + 1)`
- Evaluation metrics:
  - MAE: ~$36
  - R²: ~0.63

## 📥 Coming Soon

- Deployment guide (Streamlit Cloud or Hugging Face Spaces)
- City selector and interactive map
- Confidence intervals for predictions

---

© 2025 Dylan Martin
