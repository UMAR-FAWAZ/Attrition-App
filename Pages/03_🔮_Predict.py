# import all necessary packages
import streamlit as st 
import joblib
import pandas as pd
import os 
import datetime 

# # configure Predict page
st.set_page_config(
    page_title= 'Predict',
    page_icon=':)',
    layout= 'wide'
)

# Define function to load Gradient Boosting Machine model
st.cache_resource(show_spinner = 'Model Loading')
def load_gradient_model():
    pipeline = joblib.load('./models/gradient_pipeline.joblib')
    return pipeline

# Define function to load  Naive Bayes model
st.cache_resource(show_spinner = 'Model Loading')
def load_naive_pipeline():
    pipeline = joblib.load('./models/naives_pipeline.joblib')
    return pipeline

# Define function to select  model based on user choice
def select_model():
    col1, col2 = st.columns(2)
    with col1:
        # Dropdown to select the model
        st.selectbox('Select a model', options= ['Gradient Boosting Machines','Naive Bayes'],
                      key = 'selected_model')

    with col2:
        pass
    
    # Load the selected model
    if st.session_state['selected_model'] == 'Gradient Boosting Machines':
        pipeline = load_gradient_model()
    
    else:
        pipeline = load_naive_pipeline()

    # Load encoder for label encoding
    encoder = joblib.load('./models/encoder.joblib')
    


    return pipeline, encoder


# Ensure session_state initialization
if 'prediction' not in st.session_state:
    st.session_state['prediction'] = None
if 'probability' not in st.session_state:
    st.session_state['probability'] = None

# if not os.path.exists('./data/history.csv'):
#     os.mkdir('./data')


#define a function to make prediction
def make_prediction(pipeline, encoder):
    # Extract user input features
    gender = st.session_state['Select Gender']
    senior_citizen = st.session_state['Senior Citizen']
    partener = st.session_state['Partner']
    dependents= st.session_state['Dependents']
    tenure = st.session_state['Tenure']
    phone_service = st.session_state['Phone Service']
    multiple_lines = st.session_state['Multiple Lines']
    internet_services = st.session_state['Internet Service']
    online_security= st.session_state['Online Security']
    online_backup= st.session_state['Online Backup']
    device_protection = st.session_state['Device Protection']
    tech_support = st.session_state['Tech Support']
    streaming_tv = st.session_state['Streaming Tv']
    streaming_movies= st.session_state['Streaming Movies']
    contract= st.session_state['Contract']
    paperless_billing = st.session_state['Paperless Billing']
    payment_method = st.session_state['Payment Method']
    monthly_charges = st.session_state['Monthly Charges']
    total_charges = st.session_state['Total Charges']


    
    # Create dataframe 
    columns = [ 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
                'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
                'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
                'PaymentMethod', 'MonthlyCharges', 'TotalCharges']
    
    data = [( gender,senior_citizen, partener,dependents,tenure, phone_service,multiple_lines,
             internet_services,online_security,online_backup,device_protection,tech_support,
             streaming_tv, streaming_movies,contract,
             paperless_billing,payment_method,monthly_charges,total_charges)]
    
    df = pd.DataFrame(data, columns = columns)

    
    # Save user input data to history.csv
    df['Prediction Time'] = datetime.date.today()
    df['Selected Model'] = st.session_state['selected_model']
    df.to_csv('./data/history.csv', mode='a', header=not os.path.exists('./data/history.csv'),index=False)

    #make prediction
    pred = pipeline.predict(df)
    prediction = int(pred[0])
    prediction =  encoder.inverse_transform([prediction])

    #get probabilities
    probability = pipeline.predict_proba(df)

    # update session state
    st.session_state['prediction'] = prediction
    st.session_state['probability'] = probability


    return prediction

# Function to display user input form
def display_user_input():
    with st.spinner('Models Loading ...'):
        pipeline, encoder = select_model()

    with st.form('select-feature'):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write('### Personal Profile')
            st.selectbox('Select Gender', options=['Male', 'Female'], key = 'Select Gender')
            st.selectbox('Senior Citizen', options=['Yes', 'No'], key='Senior Citizen')
            st.selectbox('Partner', options=['Yes', 'No'], key ='Partner' )
            st.selectbox('Dependents', options=['Yes', 'No'], key = 'Dependents')


        with col2:
             
            st.write('### Service Details')
            nested_col1, nestedcol_2 =st.columns(2)
            with nested_col1:
                st.number_input('Tenure', min_value=1, max_value=72, step = 1, key ='Tenure' )
                st.selectbox('Phone Service', options=['Yes', 'No'], key = 'Phone Service' )
                st.selectbox('Multiple Lines', options=['Yes', 'No'], key='Multiple Lines' )
                st.selectbox('Internet Service', options=['DSL','Fiber optic' ,'No'], key = 'Internet Service' )
                st.selectbox('Online Security', options=['Yes', 'No'], key ='Online Security')
            with nestedcol_2:
                st.selectbox('Online Backup', options=['Yes', 'No'], key= 'Online Backup')
                st.selectbox('Device Protection', options=['Yes', 'No'], key='Device Protection' )
                st.selectbox('Tech Support', options=['Yes', 'No'], key ='Tech Support')
                st.selectbox('Streaming Tv', options=['Yes', 'No'], key= 'Streaming Tv')
                st.selectbox('Streaming Movies', options=['Yes', 'No'], key = 'Streaming Movies')


        with col3:
            st.write('### Contract and Billing')
            st.selectbox('Contract', options=  ['Month-to-month','One year' ,'Two year'], key='Contract'  )
            st.selectbox('Paperless Billing', options=['Yes', 'No'], key= 'Paperless Billing' )
            st.selectbox('Payment Method', options= ['Electronic check', 'Mailed check', 'Bank transfer (automatic)',
            'Credit card (automatic)'], key= 'Payment Method' )
            st.number_input('Monthly Charges', min_value = 29, max_value = 104, key ='Monthly Charges' )
            st.number_input('Total Charges', min_value = 29, max_value = 6845, key= 'Total Charges')

        # Submit button to make prediction 
        st.form_submit_button('Submit', on_click = make_prediction, kwargs=dict
                              (pipeline=pipeline, encoder=encoder))

if __name__ == "__main__":

     # Display title
    st.title('Make a Forecast')

    # Display user input form
    display_user_input()

    # Display prediction result
    prediction = st.session_state['prediction']
    probability = st.session_state['probability']
    
    if not prediction :
        st.markdown("### prediction will show here")
    elif prediction == "Yes":
        yes_probability = probability[0][1] *100 
        st.markdown(f"### The Employee Will Leave The Company With a Probability of {round(yes_probability, 2)}%")
    else:
        no_probability = probability[0][0]*100
        st.markdown(f"### The Employee Will Not Leave The Company, And Probability of not leaving is {round(no_probability, 2)}%")
    
    # Display session state for debugging purposes
    st.write(st.session_state) 



