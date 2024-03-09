# import all necessary packages
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# configure Dashboard page
st.set_page_config(
    page_title='Dashboard',
    page_icon='chart:)',
    layout='wide'
)

# Display Page Title
st.markdown(
    "<h1 style='text-align: center; color: white; font-size: 36px;'>Dashboard</h1>",
    unsafe_allow_html=True,
)

# Load Dataframe
df = pd.read_csv('./data/telco_churn_3000.csv')


#define function for univariate plots
def univariate_plots(df):
    st.header('Univariate Plots')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader('Histogram')
        fig = px.histogram(df, x='InternetService', nbins=10)
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.subheader('Box Plot')
        fig = px.box(df, y='MonthlyCharges')
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        st.subheader('Count Plot')
        fig = px.histogram(df, x='PhoneService', color='PhoneService')
        st.plotly_chart(fig, use_container_width=True)



# Define function for Bivariate plots
        
def bivariate_plots(df):
    st.header('Bivariate Plots')
   
   #Scatter plot of Monthly Charges vs Total Charges 
    scatter_fig = px.scatter(df, x='MonthlyCharges', y='TotalCharges', color='Churn', 
                            title='Scatter Plot of Monthly Charges vs Total Charges',
                            labels={'MonthlyCharges': 'Monthly Charges', 'TotalCharges': 'Total Charges'})
    st.plotly_chart(scatter_fig)

    #Box plot of InternetService vs MonthlyCharges
    box_fig = px.box(df, x='InternetService', y='MonthlyCharges', color='Churn', 
                    title='Box Plot of Internet Service vs Monthly Charges',
                    labels={'InternetService': 'Internet Service', 'MonthlyCharges': 'Monthly Charges'})
    st.plotly_chart(box_fig)

    #Violin plot of Contract vs MonthlyCharges
    violin_fig = px.violin(df, x='Contract', y='MonthlyCharges', color='Churn', 
                        title='Violin Plot of Contract vs Monthly Charges',
                        labels={'Contract': 'Contract', 'MonthlyCharges': 'Monthly Charges'})
    st.plotly_chart(violin_fig)
    
#Define function for MultiVariate plots
def multivariate_plots(df):
    st.header('Multivariate Plots')

    # Filter out numerical columns
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

    # Pair Plot
    st.header('Pair Plot')
    pair_fig = px.scatter_matrix(df[numerical_columns])
    st.plotly_chart(pair_fig)

    
    # Correlation Matrix
    st.header('Correlation Matrix Heatmap')
    corr = df[numerical_columns].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    correlation_heatmap = plt.gcf()  # Get the current figure
    st.pyplot(correlation_heatmap)


     # Scatter Plot
    st.header('Scatter Plot')
    scatter_x = st.selectbox("Select x-axis:", options=numerical_columns)
    scatter_y = st.selectbox("Select y-axis:", options=numerical_columns)
    scatter_fig = px.scatter(df, x=scatter_x, y=scatter_y)
    st.plotly_chart(scatter_fig)

    # Box Plot
    st.header('Box Plot')
    box_x = st.selectbox("Select column for Box Plot:", options=numerical_columns)
    box_fig = px.box(df, y=box_x)
    st.plotly_chart(box_fig)

    # Histogram
    st.header('Histogram')
    hist_col = st.selectbox("Select column for Histogram:", options=numerical_columns)
    fig, ax = plt.subplots()
    sns.histplot(data=df, x=hist_col, kde=True)
    st.pyplot(fig)

# Define function for displaying summary statistics
def display_summary_statistics(df):
    st.header('Summary Statistics')

    # Display summary statistics for all columns
    st.subheader('All Features')
    st.write(df.describe(include='all').T)

    # Display summary statistics for numerical features
    st.subheader('Numeric Features')
    st.write(df.describe().T)

    # Display summary statistics for categorical features
    st.subheader('Categorical Features')
    categorical_features = df.select_dtypes(include=['object']).columns
    for col in categorical_features:
        st.write(f"Summary statistics for '{col}'")
        st.write(df[col].value_counts())
    

# Define main section to select visualization category
if __name__ == "__main__":
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox(
            "Choose Virtualization Category",
            options=['Univariate', 'Bivariate', 'Multivariate', 'Summary Statistics'],
            key='selected_columns'
        )

    with col2:
        pass

    if st.session_state['selected_columns'] == 'Univariate':
        univariate_plots(df)

    if st.session_state['selected_columns'] == 'Bivariate':
        bivariate_plots(df)
    
    if st.session_state['selected_columns'] == 'Multivariate':
        multivariate_plots(df)

    if st.session_state['selected_columns'] == 'Summary Statistics':
        display_summary_statistics(df)