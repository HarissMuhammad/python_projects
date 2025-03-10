import streamlit as st
import pandas as pd


def main():
    print("Hello from user-project!")

    st.title("BMI Calculator")
    st.markdown("This app calculates The Body Mass Index")
    weight = st.slider("Enter Your weight in KGs", 20, 140, 45)
    height = st.slider("Enter your height (in cm)", 100, 250, 175)

    if st.button("Calculate BMI"):
        height_m = height / 100  # convert height to meters
        bmi = weight / (height_m**2)

        st.write("-" * 100)
        if bmi <= 18.5:
            st.write("You are Underweight")
        elif bmi >= 18.5 and bmi <= 24.9:
            st.write("You are Normal weight")
        elif bmi >= 25 and bmi <= 29.9:
            st.write("You are Overweight")
        elif bmi > 30:
            st.write("You are Obese")
        else:
            st.write("Something went wrong")
        st.write(f"Your BMI is {bmi:.2f}")


if __name__ == "__main__":
    main()
