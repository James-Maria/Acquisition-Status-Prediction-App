## Acquisition-Status-Prediction-App

Any company/startup old/new are prone to get closed any time. In this project, we are trying to identify if a company is closed or not, with the help of few features.

### 1. Understanding the dataset

The data is scrapped from Crunchbase, a platform to gain insights about the business information about public and private companies [https://www.crunchbase.com/]. It consists of basic information, like: name, funding, tags, ...etc.

The label of the dataset is the acquisition status of each company: Operating, IPO, Acquired, and Closed.

### 2. Data Pre - Processing

A. Data cleaning
1. Delete irrelevant and redundant information

     a. Delete 'region','city','state_code' as they provide too much of granularity.
     b. Delete 'id', 'Unnamed: 0.1', 'entity_type', 'entity_id', 'parent_id', 'created_by',
       'created_at', 'updated_at' as they are redundant.
     c. Delete 'domain', 'homepage_url', 'twitter_username', 'logo_url', 'logo_width', 'logo_height',           
        'short_description', 'description', 'overview','tag_list', 'name', 'normalized_name', 'permalink',    
        'invested_companies' as they are irrelevant features.
     d. Delete duplicate values if any.
     e. Delete those which has more than 98% of null values.

2. Remove noise or unreliable data (missing values and outliers)

     a. Delete instances with missing values for 'status', 'country_code', 'category_code' and 'founded_at'.
     b. Delete outliers for 'funding_total_usd' and 'funding_rounds'.
     c. Delete contradictory (mutually opposed or inconsistent data).
B. Data transformation
It can be divided into two successive phases.

1. Changes in original data

    a. Convert founded_at, closed_at, first_funded_at, last_funding_at, first_milestone_at ,
       last_milestone_at to years.

    b. Generalize the categorical data i.e. category_code, status and category_code - using One-Hot Encoding 

2. Creating new variables:

    a. Create new feature isClosed from closed_at and status.
        'isClosed' = 0 if 'status' = 'operating' or 'ipo'
        'isClosed' = 1 if 'status' = 'acquired' or 'closed'

    b. Create new feature 'active_days'

        'active_days' calculated using 'closed_at', 'founded_at', and 'status' to calculate the age of the company
C. Other transformations:
    1. Delete 'closed_at' column
    2. Fill null values of the numerical with the mean values of each column
    3. Drop columns with null values, i.e. 'first_investment_at', 'last_investment_at', and 'state_code'
D. Save the dataset to a new file

### 3. Feature Engineering

1. Factorize
Using the .factorize() method to transform the dataset into numerical type in order to find the correlations between them.
2. Mutual Information
Using MI to detect the most important features in the data.
It is more efficient than the correlation as it doesn't assume a linear relationship, instead it measures the level of uncertainty between two features.
3. Univariate Analysis
A. Selection with SelectKBest select the independent features which have the strongest relationship with the dependent feature Feature with the highest score will be more related to the dependent feature

B. Selection ExtraTreesClassifier Helps to give the importance of each independent feature with a dependent feature Higher score means it's more important/relevant towards output variable

4. Data Standardization
Used when all features are having high values, not 0 and 1. The mean of the independent features is 0 and the standard deviation is 1.

Save the dataset to a new file

### 4. Modelling

1. Quadratic Discriminant Analysis
Method designed to separate two or more classes based on a combination of features in a normal ditribution, where it assumes each feature has its own covariance matrix.
QDA is more flexible with high variance data.
QDA uses a classifier with a quadratic decision boundary, where each class is fitted with a Gaussian density.
This classifier was mainly used to classify between 2 classes only, Operating and Not Operating.
2. Random Forest Classifier
Classification algorithm consisting of a large number of individual decision trees that operate as an ensemble.
Each tree predicts a decision/class, and the decision with the most votes becomes the final prediction.
Low correlation between data features helps this ensemble reach better scores.
This classifier was used to classify between all 4 classes, Operating, IPO, Acquired, and Closed.
Model Validation
    1. Mean Absolute Error - the magnitude of difference between the prediction of an observation and the true value of that observation
    2. Cross Validation - tells how well a classifier generalizes, specifically the range of expected errors of the classifier.
    3. Confusion Metrix - the visual representation of the Actual VS Predicted values
    4. Classification Report - used to measure the quality of predictions from a classification algorithm.
    5. Accuracy Score - number of correctly classified prediction to the total number of prediction.
3. Predictor Function
   User defined function that combines qda_model results and rf_model results to give the final prediction.

### 5. Deployment

The application is named as AppStat (alias stat-pred). It is built using Streamlit and deployed using Streamlit as well as Heroku. 

App deployment using Streamlit
Link - https://james-maria-acquisition-status-prediction-app-appstat-akzo4k.streamlitapp.com/

App deployed via Heroku
Link - https://stat-pred.herokuapp.com/
