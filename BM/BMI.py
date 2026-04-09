pip install streamlit
import streamlit as st

st.set_page_config(page_title="BMI Calculator")
st.title("BMI Calculator")

# Input for Weight (in kg)
weight = st.number_input("Enter your weight (in kg)", min_value=1.0, value=70.0, step=0.1)

# Input for Height (in meters)
height = st.number_input("Enter your height (in meters)", min_value=0.1, value=1.75, step=0.01)

# Calculate BMI when a button is clicked
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height * height)
        st.success(f"Your BMI is: {bmi:.2f}")

        # Provide BMI categories for context
        if bmi < 18.5:
            st.warning("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("Category: Overweight")
        else:
            st.error("Category: Obesity")
    else:
        st.error("Height cannot be zero or negative. Please enter a valid height.")
