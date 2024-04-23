# Build-a-Machine-Learning-API-with-Django

This repository provides a boilerplate structure and example code to guide you in creating a RESTful API using Django that seamlessly integrates machine learning model for classification task. It combines the simplicity and flexibility of Django with the power of machine learning libraries like scikit-learn.

The inputs for Machine Learning (ML) models integrated with a Django REST Framework (DRF) API can vary depending on the specific task and chosen ML library. However, here's a general overview of common input formats:
#### JSON

{
    "Gender": "Male",
    "Married": "Yes",
    "Dependents": 2,
    "Education": "Graduate",
    "Self_Employed":"No",
    "ApplicantIncome":2333,
    "CoapplicantIncome":120,
    "LoanAmount":349,
    "Loan_Amount_Term":360,
    "Credit_History":"No",
    "Property_Area":"Urban"
  } 
  
## The task : Bank Loan Clasification:
The goal is to predict whether a loan application will be approved or not based on the provided information. The size of the dataset can vary, but it's typically around 5,000 samples. The exact number of features can differ, but it usually falls within the range of 10 to 20. Here are some common features you might encounter: 
- Customer Demographics: Age, experience (years in job), family size.
- Financial Information: Annual income, loan amount, existing debts, credit card usage.
- Banking Relationship: Mortgage status, account types (checking, savings, securities), online banking usage.<br>

  The challenge of the dataset lies on the categorical values that need to one-hot-encoded, so each time the API recieves a GET request, a function for data preprocessing and then a function for prediction are used.
