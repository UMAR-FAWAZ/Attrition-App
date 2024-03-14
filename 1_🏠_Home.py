# import all necessary packages
import streamlit as st 
import pandas as pd
import numpy as np
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


# Configure Home page
st.set_page_config(
    page_title= 'Home',
    page_icon=':)',
    layout= 'wide'
)

# Open and load configuration from YAML file
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Authenticate using credentials from the configuration
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Login with authentication credentials
name, authentication_status, username = authenticator.login(location='sidebar')

# Perform actions based on the authentication status
if st.session_state["authentication_status"]:

    # Logout if already authenticated
    authenticator.logout(location='sidebar', key='logout-button')

    # Put heading features in a container
    with st.container(border=True):
        # Add page Title
        st.markdown("<h1 style='text-align: center; color: white;'>Customer Churn Prediction App</h1>", unsafe_allow_html=True)

        # Add image
        image = "./assets\churn.jpg"

        # Adjust use_column_width
        st.image(image, use_column_width=True)

        # Write app description
        st.write(
            """This app predicts customer attrition within Vodafone, a telecommunications company in Ghana, 
            using a trained machine learning model. It identifies customers who are at risk of leaving and 
            provides insights into the contributing factors to churn. By analyzing various customer attributes 
            and behaviors, the app helps Vodafone proactively 
            address customer concerns and implement retention strategies to improve customer satisfaction and loyalty.
        """
        )

    # Divide the layout into two columns
    col1, col2 = st.columns(2)

    # Column 1: Key Features and User Benefits
    with col1:
        st.header("Key Features")
        st.markdown(
            """
                - View Data - Allows you to access the data in a remote database via connections.
                - Dashboard - Contains Data Visualization.
                - Predict - Allows you to view predictions in real-time.
                - History - Provides previous predictions made and values entered by users.
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

    # Column 2: How to run application and contact information
    with col2:
        st.header("How to run application")
        st.markdown(
            """To run the application, activate the virtual environment.
            that is, "venv/Scripts/activate".
            then run app using the Streamlit command: "streamlit rum Home.py"
            """
        )
        
        st.header("Need Help?")
        st.markdown(
            """
            Contact me at umarfawaz77@gmail.com for collaboration.
            © 2024. All rights reserved.
            """
        )

        # Add GitHub as a BUtton link
        github_link = "https://github.com/UMAR-FAWAZ"
        github_button = f'<a href="{github_link}" target="_blank"><button style="background-color: #333; color: white;">GitHub</button></a>'
        st.markdown(github_button, unsafe_allow_html=True)

        # Add LinkedIn as a Button link
        linkedin_link = "https://www.linkedin.com/in/fawaz-umar/"
        linkedin_button = f'<a href="{linkedin_link}" target="_blank"><button style="background-color: #0077B5; color: white;">LinkedIn</button></a>'
        st.markdown(linkedin_button, unsafe_allow_html=True)


elif st.session_state["authentication_status"] is False:
     # Display error message if authentication fails
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
     # Display info message and provide test account details
    st.info('Enter username and password to use the app.')
    st.code("""
            Test Account
            Username: Umar Fawaz
            Password: raf
            """)