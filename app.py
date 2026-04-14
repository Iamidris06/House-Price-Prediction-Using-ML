import streamlit as st
import joblib
import numpy as np

# Load trained Gradient Boosting model
model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction System")
st.write("Enter house details below to predict the price:")

# ---------------- Categorical Inputs ----------------
posted_by = st.selectbox("Posted By", ["Owner", "Builder", "Agent"])
under_construction = st.selectbox("Under Construction", ["Yes", "No"])
rera = st.selectbox("RERA Approved", ["Yes", "No"])
bhk_or_rk = st.selectbox("BHK or RK", ["BHK", "RK"])
ready_to_move = st.selectbox("Ready to Move", ["Yes", "No"])
resale = st.selectbox("Resale", ["Yes", "No"])

# ---------------- Numeric Inputs ----------------
bhk_no = st.number_input("Number of Bedrooms (BHK_NO.)", min_value=0)
square_ft = st.number_input("Area in SQUARE_FT", min_value=0)

# ---------------- Encoding Categorical Features ----------------
posted_by_dict = {"Owner":0, "Builder":1, "Agent":2}
under_construction_dict = {"Yes":1, "No":0}
rera_dict = {"Yes":1, "No":0}
bhk_or_rk_dict = {"BHK":0, "RK":1}
ready_to_move_dict = {"Yes":1, "No":0}
resale_dict = {"Yes":1, "No":0}

posted_by_enc = posted_by_dict[posted_by]
under_construction_enc = under_construction_dict[under_construction]
rera_enc = rera_dict[rera]
bhk_or_rk_enc = bhk_or_rk_dict[bhk_or_rk]
ready_to_move_enc = ready_to_move_dict[ready_to_move]
resale_enc = resale_dict[resale]

# ---------------- Predict Button ----------------
if st.button("Predict Price"):
    # Create input array in the same order as training features
    input_data = np.array([[posted_by_enc,
                            under_construction_enc,
                            rera_enc,
                            bhk_no,
                            bhk_or_rk_enc,
                            square_ft,
                            ready_to_move_enc,
                            resale_enc]])
    
    predicted_price = model.predict(input_data)
    st.success(f"💰 Estimated House Price: ₹ {predicted_price[0]:,.2f}")