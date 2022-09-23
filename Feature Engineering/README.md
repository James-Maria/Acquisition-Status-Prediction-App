## Feature Engineering

### 1. Mutual Information

    Using MI to detect the most important features in the data.
    It is more efficient than the correlation as it doesn't assume a linear relationship, instead it measures the level of uncertainty between two features.

### 2. Univariate Analysis

A. Selection with SelectKBest
   select the independent features which have the strongest relationship with the dependent feature
   Feature with the highest score will be more related to the dependent feature
  
B. Selection ExtraTreesClassifier
   Helps to give the importance of each independent feature with a dependent feature
   Higher score means it's more important/relevant towards output variable
   
### 3. Data Standardization

   Used when all features are having high values, not 0 and 1.
   The mean of the independent features is 0 and the standard deviation is 1.

#### Save the dataset to a new file
