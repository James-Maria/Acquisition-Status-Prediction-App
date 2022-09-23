## 1. Quadratic Discriminant Analysis

    Method designed to separate two or more classes based on a combination of features in a normal ditribution, where it assumes each feature has its own covariance matrix.
    QDA is more flexible with high variance data.
    QDA uses a classifier with a quadratic decision boundary, where each class is fitted with a Gaussian density.
    This classifier was mainly used to classify between 2 classes only, Operating and Not Operating.
    
## 2. Random Forest Classifier

    Classification algorithm consisting of a large number of individual decision trees that operate as an ensemble.
    Each tree predicts a decision/class, and the decision with the most votes becomes the final prediction.
    Low correlation between data features helps this ensemble reach better scores.
    This classifier was used to classify between all 4 classes, Operating, IPO, Acquired, and Closed.
    
 #### Model Validation

        1. Mean Absolute Error - the magnitude of difference between the prediction of an observation and the true value of that observation
        2. Cross Validation - tells how well a classifier generalizes, specifically the range of expected errors of the classifier.
        3. Confusion Metrix - the visual representation of the Actual VS Predicted values
        4. Classification Report - used to measure the quality of predictions from a classification algorithm.
        5. Accuracy Score - number of correctly classified prediction to the total number of prediction.
    
 ## 3. Predictor Function
    
       User defined function that combines qda_model results and rf_model results to give the final prediction.
