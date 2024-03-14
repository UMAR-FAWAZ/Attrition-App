# import all necessary packages
import streamlit as st 
import pyodbc
import pandas as pd
import os
from dotenv import load_dotenv
from dotenv import dotenv_values

# configure Data page
st.set_page_config(
    page_title= 'View Data',
    page_icon='📊:)',
    layout= 'wide'
)
#Page title
st.markdown(
        "<h1 style='text-align: center; color: white; font-size: 36px;'>View Datasets</h1>",
        unsafe_allow_html=True,
)



# Get data from remote Database
st.header('SQL Server Dataset')
 
 #create function to access the dataset from remote server
@st.cache_resource( show_spinner = 'DATABASE Connecting')
def get_connection():

    # Fetch connection details from secrets
    connection = pyodbc.connect(
        "DRIVER={SQL Server};SERVER="
        + st.secrets["SERVER"]
        + ";DATABASE="
        + st.secrets["DATABASE"]
        + ";UID="
        + st.secrets["USER"]
        + ";PWD="
        + st.secrets["PASSWORD"]
    )
    return connection



conn = get_connection()

#define function to query 
@st.cache_data()
def database_query(query):

    # Execute SQL query to fetch data
    with conn.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall() 
        query = "SELECT * FROM LP2_Telco_churn_first_3000"

        # Convert fetched data to DataFrame
        df = pd.DataFrame.from_records(data=rows,columns=[column[0] for column in cursor.description])
        
        # save dataframe
        df.to_csv('./data/telco_churn_3000.csv', index=False)

    return df

# # load saved data
df_save = pd.read_csv('./data/telco_churn_3000.csv')

# Check if the user is authenticated
if not st.session_state.get("authentication_status"):
    st.info('Login from the Home page to use app')
else: 

    # Define function to return all features
    @st.cache_data()
    def select_all_features():
        
        # Return all features
        df = df_save       
        return df 

    #Define function to return only numeric features
    def select_numeric_features():
        
        # Select only numeric features
        df_numeric =df_save.select_dtypes(include='number')  
    
        return df_numeric

    # Define function to return only categoric features
    def select_categoric_features():

        #Query statement
        query = "SELECT * FROM LP2_Telco_churn_first_3000"

        # Select only categorical features
        df_categoric =df_save.select_dtypes(include='object') 
        
        return df_categoric


     
    

    if __name__ == "__main__":

        # Create columns for selection box and placeholder
        col1,col2 = st.columns(2)

        with col1:

            # Selection box for choosing feature category
            st.selectbox("Choose  Feature Category",
                        options = ['All Features','Numeric Features','categoric Features'], key = 'selected_columns')

        with col2:
            pass
        
        # Check selected option and display corresponding data
        if st.session_state['selected_columns'] =="All Features":
            all_data= select_all_features()
            st.dataframe(all_data)

        if st.session_state['selected_columns'] == 'Numeric Features':
            numeric_data = select_numeric_features()
            st.dataframe(numeric_data)

        if st.session_state['selected_columns'] == 'categoric Features':
            categoric_data = select_categoric_features()
            st.dataframe(categoric_data)
        

   
        
        









