# import all necessary packages
import streamlit as st 
import pandas as pd
import numpy as np

# configure Home page
st.set_page_config(
    page_title= 'Home',
    page_icon=':)',
    layout= 'wide'
)


# put heading features in a container
with st.container(border=True):
    # Add page Title
    st.markdown("<h1 style='text-align: center; color: white;'>Customer Churn Prediction App</h1>", unsafe_allow_html=True)

    image = "images\churn.jpg"

    #Adjust use_column_width
    st.image(image, use_column_width=True)

    st.write(
        """##
        This app predicts customer attrition within Vodafone,a telecommunications company in Ghana,
        using a trained machine learning model. And pinpointing customers who are at risk of leaving
        and understanding the contributing factors to churn. 
       
    """
    )
    

col1, col2 = st.columns(2)

with col1:
    st.header("Key Features")
    st.markdown(
        """
                - View Data - Allows you to access the data in a remote database via connections.
                - Dashboard - Contains Data Vitualization.
                - Predict   - Aloows you to view prediction in a real time.
                - History   - Provides previous predictions made and values entered by users.
                
        """
    )

    st.header("User Benefits")
    st.markdown(
        """
                - Efficient Machine Learning Deployment.
                - Improved Customer Satisfaction.
                - Reduces Customer Acquisition Costs. 
                - User-Friendly Interface.
                """
    )

with col2:
    st.header("How to run application")
    st.markdown(
        """To run the application, activate the virtual environment.
        that is, "venv/Scripts/activate".
        then run app using the Streamlit command: "streamlit rum Home.py"
        """
    )
    
    st.header("Need Help?")
    st.markdown("""contact me at umarfawaz77@gmail.com for collaboration.
                © 2024. All rights reserved.
                """)