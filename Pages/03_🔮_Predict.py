import streamlit as st 
import joblib

st.set_page_config(
    page_title= 'Predict',
    page_icon=':)',
    layout= 'wide'
)

# ['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
#        'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
#        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
#        'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
#        'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn']

st.cache_resource(show_spinner = 'Model Loading')
def loed_random_model():
    pipeline = joblib.load('model/random_pipline.joblib')
    return pipeline

st.cache_resource(show_spinner = 'Model Loading')
def load_svm_pipeline():
    pipeline = joblib.load('models/svc_pipline.joblib')
    return pipeline

def select_model():
    st.selectbox('Select a model', options= ['Random Forest', 'SVC'], key = 'selected_model')
    st.title('Make a prediction')

def display_user_input():

    with st.form('select-feature'):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write('### Personal Information')
            st.number_input('Enter Age', min_value=18, max_value=60, step=2)
            st.selectbox('Select Gender', options=['Male', 'Female'])
            st.selectbox('Senior Citizen', options=['Yes', 'No'])
            st.selectbox('Partner', options=['Yes', 'No'])
            st.selectbox('Dependemts', options=['Yes', 'No'] )


        with col2:
             
            st.write('### Service Details')
            nested_col1, nestedcol_2 =st.columns(2)
            with nested_col1:
                st.number_input('Tenure', min_value=1, max_value=72, step = 1)
                st.selectbox('Phone Service', options=['Yes', 'No'] )
                st.selectbox('Multiole Lines', options=['Yes', 'No'] )
                st.selectbox('Internet Service', options=['DSL' 'Fiber optic' 'No'] )
                st.selectbox('Online Service', options=['Yes', 'No'] )
            with nestedcol_2:
                st.selectbox('Online Backup', options=['Yes', 'No'] )
                st.selectbox('Device Protection', options=['Yes', 'No'] )
                st.selectbox('Tech Support', options=['Yes', 'No'] )
                st.selectbox('Streaming Tv', options=['Yes', 'No'] )
                st.selectbox('Streaming Movies', options=['Yes', 'No'] )


        with col3:
            st.write('### Contract and Billing')
            st.selectbox('Contract', options=  ['Month-to-month','One year' ,'Two year'] )
            st.selectbox('Paperless Billing', options=['Yes', 'No'] )
            st.selectbox('Payment Method', options= ['Electronic check', 'Mailed check', 'Bank transfer',
             'Credit card'] )
            st.number_input('Monthly Charges', min_value = 29, max_value = 104)
            st.number_input('Total Charges', min_value = 29, max_value = 6845)
            
        st.form_submit_button('Submit')

if __name__ == "__main__":
    st.title('Make Prediction')
    select_model
    display_user_input()
    
    st.write(st.session_state) 