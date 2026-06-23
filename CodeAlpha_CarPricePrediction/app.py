import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Load Model
model = joblib.load(
    "car_price_prediction_model.pkl"
)

brand_goodwill = joblib.load(
    "brand_goodwill.pkl"
)

# Title
st.title("🚗 Car Price Prediction System")

st.write(
    "Predict the resale value of a used car using Machine Learning."
)

# Inputs

present_price = st.number_input(
    "Present Price (Lakhs)",
    min_value=0.0,
    value=5.0
)

kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=30000
)

owner = st.selectbox(
    "Number of Owners",
    [0,1,2,3]
)

year = st.selectbox(
    "Manufacturing Year",
    list(range(2005,2027))
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol","Diesel","CNG"]
)

selling_type = st.selectbox(
    "Selling Type",
    ["Dealer","Individual"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual","Automatic"]
)

brand = st.selectbox(
    "Brand",
    [
        "maruti",
        "hyundai",
        "honda",
        "toyota",
        "bajaj",
        "yamaha",
        "hero",
        "tvs"
    ]
)

# Prediction Button

if st.button("Predict Price"):

    current_year = datetime.now().year

    car_age = current_year - year

    goodwill = brand_goodwill.get(
        brand,
        4.0
    )

    condition_score = (
        100
        - (car_age * 2)
        - (kms_driven / 5000)
    )

    if condition_score < 0:
        condition_score = 0

    vvi = (
        0.4 * goodwill
        + 0.3 * condition_score
        + 0.3 * present_price
    )

    data = {
        "Present_Price":[present_price],
        "Driven_kms":[kms_driven],
        "Owner":[owner],
        "Car_Age":[car_age],
        "Brand_Goodwill":[goodwill],
        "Condition_Score":[condition_score],
        "VVI":[vvi]
    }

    input_df = pd.DataFrame(data)

    prediction = model.predict(
        input_df
    )[0]

    st.success(
        f"Estimated Selling Price: ₹ {prediction:.2f} Lakhs"
    )

    if prediction > present_price:
        st.info(
            "Vehicle retains high resale value."
        )

    elif prediction < present_price*0.5:
        st.warning(
            "Vehicle has depreciated significantly."
        )

    else:
        st.info(
            "Vehicle has average resale value."
        )
