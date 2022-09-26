```python
import pandas as pd # Data manipulation
import numpy as np # Numerical operations

# Plotting
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Handle warnings
import warnings
warnings.filterwarnings('ignore')
```


```python
company = pd.read_csv("companies.csv")  # import the dataset
```


```python
company.head() # 1st 5 rows
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>Unnamed: 0.1</th>
      <th>entity_type</th>
      <th>entity_id</th>
      <th>parent_id</th>
      <th>name</th>
      <th>normalized_name</th>
      <th>permalink</th>
      <th>category_code</th>
      <th>status</th>
      <th>...</th>
      <th>first_milestone_at</th>
      <th>last_milestone_at</th>
      <th>milestones</th>
      <th>relationships</th>
      <th>created_by</th>
      <th>created_at</th>
      <th>updated_at</th>
      <th>lat</th>
      <th>lng</th>
      <th>ROI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>c:1</td>
      <td>0</td>
      <td>Company</td>
      <td>1</td>
      <td>NaN</td>
      <td>Wetpaint</td>
      <td>wetpaint</td>
      <td>/company/wetpaint</td>
      <td>web</td>
      <td>operating</td>
      <td>...</td>
      <td>2010-09-05</td>
      <td>2013-09-18</td>
      <td>5.0</td>
      <td>17.0</td>
      <td>initial-importer</td>
      <td>2007-05-25 06:51:27</td>
      <td>2013-04-13 03:29:00</td>
      <td>47.606209</td>
      <td>-122.332071</td>
      <td>15.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>c:10</td>
      <td>1</td>
      <td>Company</td>
      <td>10</td>
      <td>NaN</td>
      <td>Flektor</td>
      <td>flektor</td>
      <td>/company/flektor</td>
      <td>games_video</td>
      <td>acquired</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6.0</td>
      <td>initial-importer</td>
      <td>2007-05-31 21:11:51</td>
      <td>2008-05-23 23:23:14</td>
      <td>34.021122</td>
      <td>-118.396467</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c:100</td>
      <td>2</td>
      <td>Company</td>
      <td>100</td>
      <td>NaN</td>
      <td>There</td>
      <td>there</td>
      <td>/company/there</td>
      <td>games_video</td>
      <td>acquired</td>
      <td>...</td>
      <td>2003-02-01</td>
      <td>2011-09-23</td>
      <td>4.0</td>
      <td>12.0</td>
      <td>initial-importer</td>
      <td>2007-08-06 23:52:45</td>
      <td>2013-11-04 02:09:48</td>
      <td>37.562992</td>
      <td>-122.325525</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>c:10000</td>
      <td>3</td>
      <td>Company</td>
      <td>10000</td>
      <td>NaN</td>
      <td>MYWEBBO</td>
      <td>mywebbo</td>
      <td>/company/mywebbo</td>
      <td>network_hosting</td>
      <td>operating</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-08-24 16:51:57</td>
      <td>2008-09-06 14:19:18</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c:10001</td>
      <td>4</td>
      <td>Company</td>
      <td>10001</td>
      <td>NaN</td>
      <td>THE Movie Streamer</td>
      <td>the movie streamer</td>
      <td>/company/the-movie-streamer</td>
      <td>games_video</td>
      <td>operating</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-08-24 17:10:34</td>
      <td>2008-09-06 14:19:18</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 44 columns</p>
</div>




```python
company.describe()  # Satatistical information
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0.1</th>
      <th>entity_id</th>
      <th>parent_id</th>
      <th>logo_width</th>
      <th>logo_height</th>
      <th>investment_rounds</th>
      <th>invested_companies</th>
      <th>funding_rounds</th>
      <th>funding_total_usd</th>
      <th>milestones</th>
      <th>relationships</th>
      <th>lat</th>
      <th>lng</th>
      <th>ROI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>196553.000000</td>
      <td>196553.000000</td>
      <td>0.0</td>
      <td>110110.000000</td>
      <td>110110.000000</td>
      <td>2591.000000</td>
      <td>2591.000000</td>
      <td>31707.000000</td>
      <td>2.787400e+04</td>
      <td>91699.000000</td>
      <td>129667.000000</td>
      <td>83852.000000</td>
      <td>83852.000000</td>
      <td>726.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>98276.000000</td>
      <td>153006.227333</td>
      <td>NaN</td>
      <td>459.132685</td>
      <td>222.728917</td>
      <td>2.372057</td>
      <td>2.204940</td>
      <td>1.659760</td>
      <td>1.481652e+07</td>
      <td>1.199402</td>
      <td>2.852067</td>
      <td>37.564512</td>
      <td>-52.123066</td>
      <td>45.745037</td>
    </tr>
    <tr>
      <th>std</th>
      <td>56740.108067</td>
      <td>90209.250941</td>
      <td>NaN</td>
      <td>594.982577</td>
      <td>333.090722</td>
      <td>12.173510</td>
      <td>11.436955</td>
      <td>1.201666</td>
      <td>6.775937e+07</td>
      <td>0.540099</td>
      <td>9.100309</td>
      <td>15.477102</td>
      <td>70.049067</td>
      <td>572.035638</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>NaN</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>2.910000e+02</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>-50.942326</td>
      <td>-159.497746</td>
      <td>0.011111</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>49138.000000</td>
      <td>59850.000000</td>
      <td>NaN</td>
      <td>192.000000</td>
      <td>70.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>5.000000e+05</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>34.052234</td>
      <td>-111.940005</td>
      <td>2.648879</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>98276.000000</td>
      <td>174539.000000</td>
      <td>NaN</td>
      <td>267.000000</td>
      <td>105.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>2.564500e+06</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>39.768403</td>
      <td>-77.036871</td>
      <td>6.500497</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>147414.000000</td>
      <td>232655.000000</td>
      <td>NaN</td>
      <td>484.000000</td>
      <td>232.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>1.100000e+07</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>45.421530</td>
      <td>-0.127758</td>
      <td>13.549900</td>
    </tr>
    <tr>
      <th>max</th>
      <td>196552.000000</td>
      <td>286215.000000</td>
      <td>NaN</td>
      <td>18200.000000</td>
      <td>9600.000000</td>
      <td>478.000000</td>
      <td>459.000000</td>
      <td>15.000000</td>
      <td>5.700000e+09</td>
      <td>9.000000</td>
      <td>1189.000000</td>
      <td>77.553604</td>
      <td>176.212549</td>
      <td>13333.333333</td>
    </tr>
  </tbody>
</table>
</div>




```python
company.columns # list of columns or variables
```




    Index(['id', 'Unnamed: 0.1', 'entity_type', 'entity_id', 'parent_id', 'name',
           'normalized_name', 'permalink', 'category_code', 'status', 'founded_at',
           'closed_at', 'domain', 'homepage_url', 'twitter_username', 'logo_url',
           'logo_width', 'logo_height', 'short_description', 'description',
           'overview', 'tag_list', 'country_code', 'state_code', 'city', 'region',
           'first_investment_at', 'last_investment_at', 'investment_rounds',
           'invested_companies', 'first_funding_at', 'last_funding_at',
           'funding_rounds', 'funding_total_usd', 'first_milestone_at',
           'last_milestone_at', 'milestones', 'relationships', 'created_by',
           'created_at', 'updated_at', 'lat', 'lng', 'ROI'],
          dtype='object')



## A. Data Cleaning
    1. Delete irrelevant & redundant information
    2. Remove noise or unreliable data (missing values and outliers)
    
### 1. Delete irrelevant and redundant information
     a. Delete 'region','city','state_code' as they provide too much of granularity.
     b. Delete 'id', 'Unnamed: 0.1', 'entity_type', 'entity_id', 'parent_id', 'created_by',
       'created_at', 'updated_at' as they are redundant.
     c. Delete 'domain', 'homepage_url', 'twitter_username', 'logo_url', 'logo_width', 'logo_height',           
        'short_description', 'description', 'overview','tag_list', 'name', 'normalized_name', 'permalink',    
        'invested_companies' as they are irrelevant features.
     d. Delete duplicate values if any.
     e. Delete those which has more than 98% of null values.
     
### 2. Remove noise or unreliable data (missing values and outliers)
     a. Delete instances with missing values for 'status', 'country_code', 'category_code' and 'founded_at'.
     b. Delete outliers for 'funding_total_usd' and 'funding_rounds'.
     c. Delete contradictory (mutually opposed or inconsistent data).

#### 1.a. Delete 'region','city' as they provide too much of granularity.    


```python
company.drop(['region', 'city', 'state_code'], axis = 1, inplace = True) 
```

#### 1.b. Delete 'id', 'Unnamed: 0.1', 'entity_type', 'entity_id', 'parent_id', 'created_by', 'created_at', 'updated_at' as they are redundant.


```python
company.drop(['id', 'Unnamed: 0.1', 'entity_type', 'entity_id', 'parent_id', 'created_by','created_at', 'updated_at'], 
             axis = 1, inplace = True) 
```

#### 1.c. Delete 'domain', 'homepage_url', 'twitter_username', 'logo_url', 'logo_width', 'logo_height',  'short_description',    'description',  'overview','tag_list', 'name', 'normalized_name', 'permalink', 'invested_companies' as they are irrelevant features.


```python
company.drop(['domain', 'homepage_url', 'twitter_username', 'logo_url','logo_width', 'logo_height', 'short_description', 
              'description', 'overview', 'tag_list', 'name','normalized_name', 'permalink', 'invested_companies'], 
             axis = 1, inplace = True) 
```

#### 1.d. Delete duplicate values if found any.


```python
company.duplicated().sum() # count of duplicated values
```




    87089




```python
company.drop_duplicates(inplace=True) # delete duplicates
```


```python
# check if any left
company.duplicated().sum()
```




    0



#### 1.e. Delete those which has more than 98% of null values.


```python
company.isna().sum() # number of null values per column
```




    category_code           12230
    status                      0
    founded_at              26913
    closed_at              106845
    country_code            24870
    first_investment_at    107217
    last_investment_at     107217
    investment_rounds      107213
    first_funding_at        77992
    last_funding_at         77992
    funding_rounds          77793
    funding_total_usd       81602
    first_milestone_at      53353
    last_milestone_at       53353
    milestones              53353
    relationships           34403
    lat                     28363
    lng                     28363
    ROI                    108738
    dtype: int64




```python
company.isna().any(axis = 1).sum() # total number of null values
```




    109464




```python
col_percent = pd.DataFrame(company.isnull().sum() * 100 / len(company)) # percentage of null values
col_percent
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>category_code</th>
      <td>11.172623</td>
    </tr>
    <tr>
      <th>status</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>founded_at</th>
      <td>24.586165</td>
    </tr>
    <tr>
      <th>closed_at</th>
      <td>97.607433</td>
    </tr>
    <tr>
      <th>country_code</th>
      <td>22.719798</td>
    </tr>
    <tr>
      <th>first_investment_at</th>
      <td>97.947270</td>
    </tr>
    <tr>
      <th>last_investment_at</th>
      <td>97.947270</td>
    </tr>
    <tr>
      <th>investment_rounds</th>
      <td>97.943616</td>
    </tr>
    <tr>
      <th>first_funding_at</th>
      <td>71.248995</td>
    </tr>
    <tr>
      <th>last_funding_at</th>
      <td>71.248995</td>
    </tr>
    <tr>
      <th>funding_rounds</th>
      <td>71.067200</td>
    </tr>
    <tr>
      <th>funding_total_usd</th>
      <td>74.546883</td>
    </tr>
    <tr>
      <th>first_milestone_at</th>
      <td>48.740225</td>
    </tr>
    <tr>
      <th>last_milestone_at</th>
      <td>48.740225</td>
    </tr>
    <tr>
      <th>milestones</th>
      <td>48.740225</td>
    </tr>
    <tr>
      <th>relationships</th>
      <td>31.428598</td>
    </tr>
    <tr>
      <th>lat</th>
      <td>25.910802</td>
    </tr>
    <tr>
      <th>lng</th>
      <td>25.910802</td>
    </tr>
    <tr>
      <th>ROI</th>
      <td>99.336768</td>
    </tr>
  </tbody>
</table>
</div>




```python
# drop columns with more then 98% null values
for col in col_percent.index:
    if col_percent.loc[col,0] > 98:
        company.drop(col, axis = 1, inplace=True)
```

#### 2.a. Delete instances with missing values for 'status', 'country_code', 'category_code' and 'founded_at'.
    (Since these are the type of data where adding value via imputation will create wrong pattern only)


```python
company = company.dropna( how='any',subset=['status', 'country_code', 'category_code','founded_at'])
```


```python
company.isna().any(axis=1).sum() # total null values
```




    63581



#### 2.b. Delete outliers for 'funding_total_usd' and 'funding_rounds'.


```python
sns.boxplot(company['funding_total_usd'])
```




    <AxesSubplot:xlabel='funding_total_usd'>




    
![png](output_25_1.png)
    



```python
np.where(company['funding_total_usd'] > 1.0e9)
```




    (array([ 1173,  1543,  2344, 17438, 25745, 29511, 44165, 49090, 53118,
            54984, 55189, 57302], dtype=int64),)




```python
sns.boxplot(company['funding_rounds'])
```




    <AxesSubplot:xlabel='funding_rounds'>




    
![png](output_27_1.png)
    



```python
np.where(company['funding_rounds'] >= 4)
```




    (array([    7,    40,    77, ..., 63491, 63556, 63569], dtype=int64),)



we can see the outlier in both 'funding_total_usd' and 'funding_rounds'. So, let's find them and drop it.

    1. Find the IQR (Interquartile Range)
    2. Find the upper and lower limit
    3. Find outliers
    4. Drop them
    5. Compare the plots after trimming 


#### 2.b.1. Find the IQR


```python
# For funding_total_usd
Q1_ftu = company.funding_total_usd.quantile(0.25)
 
Q3_ftu = company.funding_total_usd.quantile(0.75)

IQR_ftu = Q3_ftu - Q1_ftu

# For funding_rounds
Q1_fr = company.funding_rounds.quantile(0.25)
 
Q3_fr = company.funding_rounds.quantile(0.75)

IQR_fr = Q3_fr - Q1_fr

```

#### 2.b.1. Find the Upper and Lower limit


```python
# For funding_total_usd
upper_ftu = Q3_ftu+1.5*IQR_ftu
lower_ftu = Q1_ftu-1.5*IQR_ftu

# For funding_rounds
upper_fr = Q3_fr+1.5*IQR_fr
lower_fr = Q1_fr-1.5*IQR_fr
```

#### 2.b.1.  Find outliers


```python
# For funding_total_usd
outlier_ftu = company.loc[(company.funding_total_usd < lower_ftu) | (company.funding_total_usd > upper_ftu)]

# For funding_rounds
outlier_fr = company.loc[(company.funding_rounds < lower_fr) | (company.funding_rounds > upper_fr)]
```

#### 2.b.1. Drop the outliers


```python
# For funding_total_usd
company = company.loc[(company.funding_total_usd > lower_ftu) & (company.funding_total_usd < upper_ftu)]

# For funding_rounds
company = company.loc[(company.funding_rounds > lower_fr) & (company.funding_rounds < upper_fr)]
   
```

# B. Date Transformation
    It can be divided into two successive phases.
   ## 1. Changes in original data
        a. Convert founded_at, closed_at, first_funded_at, last_funding_at, first_milestone_at ,
           last_milestone_at to years.
        b. Generalize the categorical data i.e. category_code, status and category_code.
   ## 2. Create new variables
        a. Create new feature isClosed from closed_at and status.
        b. Create new feature 'active_days'

#### 1.a. Convert founded_at, closed_at, first_funded_at, last_funding_at, first_milestone_at , last_milestone_at to years.


```python
from datetime import datetime
```


```python
date_columns = ['founded_at', 'closed_at', 'first_funding_at', 'last_funding_at', 'first_milestone_at', 'last_milestone_at']

for col in date_columns:
    company[col] = pd.to_datetime(company[col]).dt.year
```

 #### 1.b. Generalize the categorical data i.e. category_code and  country_code 


```python
from sklearn.preprocessing import OneHotEncoder
```


```python
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
```


```python
OH_company = pd.DataFrame(OH_encoder.fit_transform(company[['category_code', 'country_code']]))
```


```python
# One-hot encoding removed index; put it back
OH_company.index = company.index
```


```python
# Remove categorical columns (will replace with one-hot encoding)
company = company.drop(['category_code', 'country_code'], axis=1)
```


```python
# Add one-hot encoded columns to numerical features
company = pd.concat([company, OH_company], axis=1)
```

### 2. Create new variables¶
    a. Create new feature isClosed from closed_at and status.
    b. Create new feature 'active_days'

#### 2.a. Create new feature isClosed from closed_at and status.
     - if the value in status is 'operating' or 'ipo', Let's put 1.
     - Where as if the value is 'acquired' or 'closed', let's put 0.


```python
for i in list(company.index):
    company.loc[company['status'] == 'operating', 'isClosed'] = 1
    company.loc[company['status'] == 'ipo', 'isClosed'] = 1
    company.loc[company['status'] == 'acquired', 'isClosed'] = 0
    company.loc[company['status'] == 'closed', 'isClosed'] = 0
```


```python
company
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>status</th>
      <th>founded_at</th>
      <th>closed_at</th>
      <th>first_investment_at</th>
      <th>last_investment_at</th>
      <th>investment_rounds</th>
      <th>first_funding_at</th>
      <th>last_funding_at</th>
      <th>funding_rounds</th>
      <th>funding_total_usd</th>
      <th>...</th>
      <th>141</th>
      <th>142</th>
      <th>143</th>
      <th>144</th>
      <th>145</th>
      <th>146</th>
      <th>147</th>
      <th>148</th>
      <th>149</th>
      <th>isClosed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13</th>
      <td>acquired</td>
      <td>2007</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008.0</td>
      <td>2008.0</td>
      <td>1.0</td>
      <td>5000000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>operating</td>
      <td>2003</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2011.0</td>
      <td>2012.0</td>
      <td>3.0</td>
      <td>10125293.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>operating</td>
      <td>2003</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2003.0</td>
      <td>2003.0</td>
      <td>1.0</td>
      <td>250000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>32</th>
      <td>operating</td>
      <td>2010</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2011.0</td>
      <td>2011.0</td>
      <td>1.0</td>
      <td>100000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>36</th>
      <td>operating</td>
      <td>2006</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2011.0</td>
      <td>2012.0</td>
      <td>2.0</td>
      <td>11300000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>196526</th>
      <td>closed</td>
      <td>2008</td>
      <td>2012.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008.0</td>
      <td>2008.0</td>
      <td>1.0</td>
      <td>130000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>196537</th>
      <td>operating</td>
      <td>2011</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2011.0</td>
      <td>2011.0</td>
      <td>1.0</td>
      <td>500000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>196540</th>
      <td>closed</td>
      <td>2006</td>
      <td>2012.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008.0</td>
      <td>2009.0</td>
      <td>2.0</td>
      <td>1100000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>196549</th>
      <td>operating</td>
      <td>2007</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008.0</td>
      <td>2008.0</td>
      <td>1.0</td>
      <td>750000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>196552</th>
      <td>operating</td>
      <td>2007</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008.0</td>
      <td>2008.0</td>
      <td>1.0</td>
      <td>475000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
<p>16880 rows × 167 columns</p>
</div>



#### 2.b. Create active_days
     i. Replacing values:
         -  if the value in status is 'operating' or 'ipo' in closed_at, Let's put 2021.
         - Where as if the value is 'acquired' or 'closed', let's put 0.
     ii. Subtract founded_date from closed_date, and calculate age in days (After calculating active days, 
         check contradictory issues we didn't check it before).
     iii. Then, delete the closed_at column.

##### 2.b.i  Replacing the values in closed_at column
   - if the value in status is 'operating' or 'ipo' in closed_at, Let's put 2021.
   - Where as if the value is 'acquired' or 'closed', let's put 0.


```python
for i in list(company.index):
    company.loc[company['status'] == 'operating', 'closed_at'] = 2021
    company.loc[company['status'] == 'ipo', 'closed_at'] = 2021
    company.loc[company['status'] == 'acquired', 'closed_at'] = 0
    company.loc[company['status'] == 'closed', 'closed_at'] = 0
```

##### 2.b.ii Subtract founded_date from closed_date, and calculate age in days (After calculating active days, check contradictory issues we didn't check it before.)


```python
company['active_days'] = abs((company.closed_at - company.founded_at) * 365)
company
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>status</th>
      <th>founded_at</th>
      <th>closed_at</th>
      <th>first_investment_at</th>
      <th>last_investment_at</th>
      <th>investment_rounds</th>
      <th>first_funding_at</th>
      <th>last_funding_at</th>
      <th>funding_rounds</th>
      <th>funding_total_usd</th>
      <th>...</th>
      <th>142</th>
      <th>143</th>
      <th>144</th>
      <th>145</th>
      <th>146</th>
      <th>147</th>
      <th>148</th>
      <th>149</th>
      <th>isClosed</th>
      <th>active_days</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13</th>
      <td>acquired</td>
      <td>2007</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008.0</td>
      <td>2008.0</td>
      <td>1.0</td>
      <td>5000000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>732555.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>operating</td>
      <td>2003</td>
      <td>2021.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2011.0</td>
      <td>2012.0</td>
      <td>3.0</td>
      <td>10125293.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>6570.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>operating</td>
      <td>2003</td>
      <td>2021.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2003.0</td>
      <td>2003.0</td>
      <td>1.0</td>
      <td>250000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>6570.0</td>
    </tr>
    <tr>
      <th>32</th>
      <td>operating</td>
      <td>2010</td>
      <td>2021.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2011.0</td>
      <td>2011.0</td>
      <td>1.0</td>
      <td>100000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>4015.0</td>
    </tr>
    <tr>
      <th>36</th>
      <td>operating</td>
      <td>2006</td>
      <td>2021.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2011.0</td>
      <td>2012.0</td>
      <td>2.0</td>
      <td>11300000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>5475.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>196526</th>
      <td>closed</td>
      <td>2008</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008.0</td>
      <td>2008.0</td>
      <td>1.0</td>
      <td>130000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>732920.0</td>
    </tr>
    <tr>
      <th>196537</th>
      <td>operating</td>
      <td>2011</td>
      <td>2021.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2011.0</td>
      <td>2011.0</td>
      <td>1.0</td>
      <td>500000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>3650.0</td>
    </tr>
    <tr>
      <th>196540</th>
      <td>closed</td>
      <td>2006</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008.0</td>
      <td>2009.0</td>
      <td>2.0</td>
      <td>1100000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>732190.0</td>
    </tr>
    <tr>
      <th>196549</th>
      <td>operating</td>
      <td>2007</td>
      <td>2021.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008.0</td>
      <td>2008.0</td>
      <td>1.0</td>
      <td>750000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>5110.0</td>
    </tr>
    <tr>
      <th>196552</th>
      <td>operating</td>
      <td>2007</td>
      <td>2021.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008.0</td>
      <td>2008.0</td>
      <td>1.0</td>
      <td>475000.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>5110.0</td>
    </tr>
  </tbody>
</table>
<p>16880 rows × 168 columns</p>
</div>



#### 2.b.iii. Then, delete the closed_at column.


```python
company.drop('closed_at', axis = 1, inplace = True)
```

### Delete the columns with Null values


```python
company.drop(['first_investment_at', 'last_investment_at', 'investment_rounds'], axis = 1, inplace = True)
```

### Remove the null vaues with the mean value in 'Numerical Data'


```python
company['funding_total_usd'] = company['funding_total_usd'].fillna(company.funding_total_usd.mean())

company['funding_rounds'] = company['funding_rounds'].fillna(company.funding_rounds.mean())

company['milestones'] = company['milestones'].fillna(company.milestones.mean())

company['relationships'] = company['relationships'].fillna(company.relationships.mean())
```


```python
company.isna().sum().sum() # count of null values
```




    14658




```python
company.dropna(inplace=True) # drop null values
```


```python
# First let's check how much of rows has nan values and drop them.
company.isna().sum().sum()
```




    0




```python
# Save cleaned Data.
company.index = range(0,len(company))
company.to_csv('companies_new.csv')
```


```python
company
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>status</th>
      <th>founded_at</th>
      <th>first_funding_at</th>
      <th>last_funding_at</th>
      <th>funding_rounds</th>
      <th>funding_total_usd</th>
      <th>first_milestone_at</th>
      <th>last_milestone_at</th>
      <th>milestones</th>
      <th>relationships</th>
      <th>...</th>
      <th>142</th>
      <th>143</th>
      <th>144</th>
      <th>145</th>
      <th>146</th>
      <th>147</th>
      <th>148</th>
      <th>149</th>
      <th>isClosed</th>
      <th>active_days</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>acquired</td>
      <td>2007</td>
      <td>2008.0</td>
      <td>2008.0</td>
      <td>1.0</td>
      <td>5000000.0</td>
      <td>2008.0</td>
      <td>2012.0</td>
      <td>3.0</td>
      <td>14.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>732555.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>operating</td>
      <td>2003</td>
      <td>2011.0</td>
      <td>2012.0</td>
      <td>3.0</td>
      <td>10125293.0</td>
      <td>2010.0</td>
      <td>2010.0</td>
      <td>1.0</td>
      <td>6.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>6570.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>operating</td>
      <td>2003</td>
      <td>2003.0</td>
      <td>2003.0</td>
      <td>1.0</td>
      <td>250000.0</td>
      <td>2007.0</td>
      <td>2007.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>6570.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>operating</td>
      <td>2004</td>
      <td>2011.0</td>
      <td>2011.0</td>
      <td>1.0</td>
      <td>1500000.0</td>
      <td>2010.0</td>
      <td>2010.0</td>
      <td>1.0</td>
      <td>8.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>6205.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>operating</td>
      <td>2006</td>
      <td>2007.0</td>
      <td>2007.0</td>
      <td>1.0</td>
      <td>2500000.0</td>
      <td>2010.0</td>
      <td>2012.0</td>
      <td>2.0</td>
      <td>7.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>5475.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9803</th>
      <td>closed</td>
      <td>2008</td>
      <td>2008.0</td>
      <td>2008.0</td>
      <td>1.0</td>
      <td>130000.0</td>
      <td>2008.0</td>
      <td>2009.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>732920.0</td>
    </tr>
    <tr>
      <th>9804</th>
      <td>operating</td>
      <td>2011</td>
      <td>2011.0</td>
      <td>2011.0</td>
      <td>1.0</td>
      <td>500000.0</td>
      <td>2011.0</td>
      <td>2011.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>3650.0</td>
    </tr>
    <tr>
      <th>9805</th>
      <td>closed</td>
      <td>2006</td>
      <td>2008.0</td>
      <td>2009.0</td>
      <td>2.0</td>
      <td>1100000.0</td>
      <td>2005.0</td>
      <td>2008.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>732190.0</td>
    </tr>
    <tr>
      <th>9806</th>
      <td>operating</td>
      <td>2007</td>
      <td>2008.0</td>
      <td>2008.0</td>
      <td>1.0</td>
      <td>750000.0</td>
      <td>2013.0</td>
      <td>2013.0</td>
      <td>1.0</td>
      <td>14.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>5110.0</td>
    </tr>
    <tr>
      <th>9807</th>
      <td>operating</td>
      <td>2007</td>
      <td>2008.0</td>
      <td>2008.0</td>
      <td>1.0</td>
      <td>475000.0</td>
      <td>2006.0</td>
      <td>2008.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>5110.0</td>
    </tr>
  </tbody>
</table>
<p>9808 rows × 164 columns</p>
</div>




```python

```
