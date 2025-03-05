import streamlit as st

print("Last three games : 3 "
      " Goals : 8")

print("Last three games : 3 "
      " Goals : 8")

if st.button("Click"):
    st.write("Clicked")

st.title("BMI Calculator")
st.markdown("This app calculates The Body Mass Index")
weight = st.number_input("Enter Your weight in KGs", step=0.1)
height = st.number_input("Enter your height (in cm)", step=0.1)

if st.button("Calculate BMI"):
    if height > 0:
        height_m = height / 100  # convert height to meters
        bmi = weight / (height_m ** 2)
        st.write(f"Your BMI is {bmi:.2f}")
    else:
        st.write("Please enter a valid height.")