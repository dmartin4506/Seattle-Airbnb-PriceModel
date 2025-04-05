import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and features
model = joblib.load("model/airbnb_model.pkl")
feature_names = joblib.load("model/model_features.pkl")

# Title and instructions
st.title("🏠 Airbnb Price Predictor – Seattle")
st.write("Enter your listing details to predict a nightly price (based on Seattle Airbnb data).")

# Input form
room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room"])
available_neighborhoods = sorted([col.replace("neighbourhood_cleansed_", "") 
                                  for col in feature_names 
                                  if col.startswith("neighbourhood_cleansed_")])

neighbourhood = st.selectbox("Neighbourhood", available_neighborhoods)

accommodates = st.slider("Accommodates (Guests)", 1, 10, 2)
bedrooms = st.slider("Bedrooms", 0, 5, 1)
beds = st.slider("Beds", 1, 10, 1)
bathrooms = st.slider("Bathrooms", 1.0, 4.0, 1.0, step=0.5)
minimum_nights = st.slider("Minimum Nights", 1, 30, 2)
availability_365 = st.slider("Availability (days per year)", 0, 365, 180)
review_scores_rating = st.slider("Review Score", 0.0, 100.0, 95.0)

# Coordinates for location
latitude = st.number_input("Latitude", value=47.6205)
longitude = st.number_input("Longitude", value=-122.3493)

# Amenities (checklist)
st.markdown("**Amenities**")
has_wifi = st.checkbox("WiFi", value=True)
has_kitchen = st.checkbox("Kitchen", value=True)
has_tv = st.checkbox("TV")
has_heating = st.checkbox("Heating", value=True)
has_washer = st.checkbox("Washer")
has_dryer = st.checkbox("Dryer")
has_air_conditioning = st.checkbox("Air Conditioning")
has_free_parking = st.checkbox("Free Parking")

# Calculate distance to downtown (Pike Place)
center_lat = 47.6097
center_lon = -122.3425
distance_to_downtown = np.sqrt((latitude - center_lat)**2 + (longitude - center_lon)**2)

# Construct input DataFrame
input_data = pd.DataFrame([{
    "accommodates": accommodates,
    "bedrooms": bedrooms,
    "beds": beds,
    "bathrooms": bathrooms,
    "minimum_nights": minimum_nights,
    "availability_365": availability_365,
    "review_scores_rating": review_scores_rating,
    "latitude": latitude,
    "longitude": longitude,
    "distance_to_downtown": distance_to_downtown,
    "has_wifi": int(has_wifi),
    "has_kitchen": int(has_kitchen),
    "has_tv": int(has_tv),
    "has_heating": int(has_heating),
    "has_washer": int(has_washer),
    "has_dryer": int(has_dryer),
    "has_air_conditioning": int(has_air_conditioning),
    "has_free_parking": int(has_free_parking),
    f"room_type_{room_type}": 1,
    f"neighbourhood_cleansed_{neighbourhood}": 1
}])

# Fill missing columns with 0s
# Fill any missing feature columns with 0
for col in feature_names:
    if col not in input_data.columns:
        input_data[col] = 0

# Reorder columns to match training data
input_data = input_data[feature_names]

# Add a predict button
if st.button("🚀 Predict Price"):
    log_price = model.predict(input_data)[0]
    price = np.expm1(log_price)
    st.subheader(f"💵 Estimated Nightly Price: ${price:.2f}")
