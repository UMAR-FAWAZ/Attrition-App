# # import all necessary packages
import streamlit as st 
import pyodbc
import pandas as pd
import os
from dotenv import load_dotenv
from dotenv import dotenv_values

# configure Data page
st.set_page_config(
    page_title= 'View Data',
    page_icon=':)',
    layout= 'wide'
)
st.markdown(
        "<h1 style='text-align: center; color: white; font-size: 36px;'>View Data</h1>",
        unsafe_allow_html=True,
)


st.header('SQL server Data')
# Get data from remote Database 

# Load environment variables from .env file 
environment_variables = dotenv_values('.env')


# Get the values for the credentials in the '.env' file
database = environment_variables.get("DATABASE")
server = environment_variables.get("SERVER")
username = environment_variables.get("USER")
password = environment_variables.get("PASSWORD")

# Create a connection string
connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};MARS_Connection=yes;MinProtocolVersion=TLSv1.2;"

# Use the connect method of the pyodbc library and pass in the connection string.
connection = pyodbc.connect(connection_string)

# Execute the query and fetch the results
query = "SELECT * FROM LP2_Telco_churn_first_3000"
results = pd.read_sql(query, connection)

#display the results in streamlit 
st.dataframe(results)



st.header('GitHub Data ')
# # Get data from Github repo

# Provide the link to the raw content of the CSV file on GitHub
github_url = "https://raw.githubusercontent.com/Azubi-Africa/Career_Accelerator_LP2-Classifcation/main/LP2_Telco-churn-second-2000.csv"

# Read data from the raw GitHub URL
df_github = pd.read_csv(github_url)

# Display GitHub data
st.dataframe(df_github)

# concantenate the two dataframes
st.header('Dataframes Combined ')
data_train = pd.concat([results, df_github])

st.dataframe(data_train)