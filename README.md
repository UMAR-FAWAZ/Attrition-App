<a name="readme-top"></a>

<div align="center">
  <h1><b>Customer Churn Prediction App</b></h1>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📗 Table of Contents](#-table-of-contents)
- [Prediction Insight ](#prediction-insight-)
  - [🛠 Built With ](#-built-with-)
    - [Tech Stack ](#tech-stack-)
  - [Key Features ](#key-features-)
  - [💻 Getting Started ](#-getting-started-)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Install](#install)
    - [Usage](#usage)
  - [👥 Authors ](#-authors-)
  - [🔭 Future Features ](#-future-features-)
  - [🤝 Contributing ](#-contributing-)
  - [⭐️ Show your support ](#️-show-your-support-)
  - [🙏 Acknowledgments ](#-acknowledgments-)
  - [📝 License ](#-license-)

<!-- PROJECT DESCRIPTION -->

# Customer Churn App <a name="about-project"></a>

**Prediction Insight:** Deploying Machine Learning Models with Streamlit to Predict Customers that Churn in a Telecommunication Company. The application allows users to interact with a machine learning model, view data visualizations on the data and see the values of their input saved for future use.

**Features**

 Below is the describtion of the columns present in the data :
1. **Gender**: Gender of customers [Male or Female]
2. **SeniorCitizen**: Customer citizenship status [Yes or No]
3. **Partner**: Whether the customer has a partner or not [Yes or NO]
4. **Dependents**: Whether the customer has dependents or not [Yes or No]
5. **Tenure**:  Number of months the customer has stayed with the company
6. **Phone Service**: Customer has a phone service or not [Yes or No] 
7. **MultipleLines**: Customer has multiple lines or not [Yes or No]
8. **InternetService**: Customer's internet service provider [DSL, Fiber Optic, No]
9. **OnlineSecurity**: Customer has online security or not [Yes, No]
10. **OnlineBackup**: customer has online backup or not [Yes, No]
11. **DeviceProtection**: Customer has device protection or not [Yes, No]
12. **TechSupport**: Customer has tech support or not [Yes, No]
13. **StreamingTV**: Whether the customer has streaming TV or not [Yes, No]
14. **StreamingMovies**: Whether the customer has streaming movies or not [Yes, No]
15. **Contract**: The contract term of the customer [Month-to-Month, One year, Two year]
16. **PaperlessBilling**: Customer has paperless billing or not [Yes, No]
17. **Payment Method**: The customer's payment method [Electronic check, mailed check, Bank transfer(automatic), Credit card(automatic)]
18. **MonthlyCharges**: Customer monthly amount charged
19. **TotalCharges**: Customer total amount charged
20. **Churn**: Customer churned or not [Yes or No]

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
  <summary>GUI</summary>
  <ul>
    <li><a href="">Streamlit</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="">Microsoft SQL Server</a></li>
  </ul>
</details>

<details>
<summary>Language</summary>
  <ul>
    <li><a href="">Python</a></li>
  </ul>
</details>

<details>
<summary>Model</summary>
  <ul>
    <li><a href="">Sklearn</a></li>
  </ul>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- Features -->

## Key Features <a name="key-features"></a>

- **View Data - Allows you to access the data in a remote database via connections.**
- **Dashboard - Contains Data Vitualization.**
- **Predicitons - page allows you to view prediction in a real time, by specifying the model they want to use**
- **History   - Provides previous predictions made and values entered by users.**


<p align="right">(<a href="#readme-top">back to top</a>)</p>

![Image](https://github.com/UMAR-FAWAZ/Attrition-App/blob/main/assets/visual.png)


<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>


To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python

### Setup

Clone this repository to your desired folder:


```sh
  cd my-folder
  git clone https://github.com/UMAR-FAWAZ/Attrition-App.git
```

Change into the cloned repository

```sh
  cd Attrition-App
  
```

Create a virtual environment

```sh

python -m venv venv

```

Activate the virtual environment

```sh
    venv/Scripts/activate
```


### Install

Here, you need to recursively install the packages in the `requirements.txt` file using the command below 

```sh
   pip install -r requirements.txt
```


### Usage

To run the project, execute the following command:


```sh
    streamlit run 1_🏠_Home.py

```

- A webpage opens up to view the app
- Login to the app with `username=umarfawaz` and `password:jat`
- Finally test a prediction by clicking on the predicitons page
- **Note**: Users may not be able to access the View Data page as the secrets file is not checked into git

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

🕵🏽‍♀️ **Umar Fawaz**

- GitHub: [GitHub Profile](https://github.com/UMAR-FAWAZ/Attrition-App)
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/fawaz-umar)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a name="future-features"></a>


- **Add a front end application for users**
  
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

I would like to thank all the free available resource made available online and Azubi Africa

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


