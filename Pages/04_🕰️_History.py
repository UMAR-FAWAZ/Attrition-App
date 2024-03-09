# import all necessary packages
import streamlit as st
import pandas as pd

# configure History page
st.set_page_config(
    page_title= 'History',
    page_icon=':)',
    layout= 'wide'
)

# Add Page title
st.markdown(
        "<h1 style='text-align: center; color: white; font-size: 36px;'>Prediction History</h1>",
        unsafe_allow_html=True,
)

# Define function to retrieve prediction history from CSV file
def retrieve_prediction_history():
    csv_path = "./data/history.csv"
    df = pd.read_csv(csv_path)
    return df


# Main function to display prediction history
if __name__ =='__main__':
    df = retrieve_prediction_history() # Retrieve prediction history DataFrame
    st.dataframe(df) # Display the DataFrame in Streamlit

