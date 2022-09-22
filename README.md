# Acquisition Status Prediction App

Any company and/or startup, old or new, is prone to fail at any moment. Here, we aim to predict whether the company is operating or not, based on a given set of features.

### Understanding the dataset
The data is scrapped from Crunchbase, a platform to gain insights about the business information about public and private companies [https://www.crunchbase.com/]. It consists of basic information, like: name, funding, tags, ...etc.

The label of the dataset is the acquisition status of each company: Operating, IPO, Acquired, and Closed.

### Preprocessing

#### A. Data cleaning

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
 
#### B. Data transformation

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
        
#### C. Other transformations:

        1. Delete 'closed_at' column
        2. Fill null values of the numerical with the mean values of each column
        3. Drop columns with null values, i.e. 'first_investment_at', 'last_investment_at', and 'state_code'
        
#### D. Save the dataset to a new file
