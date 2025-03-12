import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


def main():
    print("Hello from python-website!")
    st.title("Dashboard")
    uploaded_file = st.file_uploader("Upload the CSV file", type="csv")
    if uploaded_file != None:
        st.write("File Uploaded")
        df = pd.read_csv(uploaded_file)

        st.subheader("Data Preview")
        st.write(df.head())

        st.subheader("Summary")
        st.write(df.describe())

        st.subheader("Filter Data")
        col = df.columns.to_list()
        selected_col = st.selectbox("Select columns to filter by :", col)
        unique = df[selected_col].unique()
        selected_val = st.selectbox("Select value ", unique)

        filtered_df = df[df[selected_col] == selected_val]
        st.write(filtered_df)

        st.subheader("Plot data")

        x = st.selectbox("Select the x coloumn ", col)
        y = st.selectbox("Select the y coloumn ", col)

        if st.button("Generate Plot"):
            st.line_chart(filtered_df.set_index(x)[y])
    else:
        st.write("Waiting for the file to be uploaded")


if __name__ == "__main__":
    main()
