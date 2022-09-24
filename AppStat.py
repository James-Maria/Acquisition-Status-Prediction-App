import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

def Predictor(to_predict, model_qda, model_rf):
    # size = len(to_predict_list)
    # to_predict = np.array(to_predict_list).reshape(1, size)

    preds = model_qda.predict(to_predict)
    # 0 : operating, 1 : closed
    if preds == 1:
        out = 'Operating'
    else:
        pred = model_rf.predict(to_predict)
        # result = str(preds[0])
        # 0 : acquired, 1 : operating, 2 : closed, 3 : ipo
        if pred == 0:
            out = 'Acquired'
        elif pred == 1:
            out = 'Operating'
        elif pred == 2:
            out = 'Closed'
        else:
            out = 'IPO'

    return out


df = pd.read_csv('new_companies.csv')
df.drop(['Unnamed: 0'], axis=1, inplace=True)

sc = StandardScaler()

X = df.drop(['isClosed', 'status'], axis = 1)
y = df['isClosed']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
qda_model = QuadraticDiscriminantAnalysis()
qda_model.fit(X_train, y_train)

X = df.drop(['status', 'isClosed'], axis = 1)
y = df['status']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(X_train, y_train)

ch = []

st.markdown("<h1 style='text-align: center;'>Startup Acquisition Status Prediction App</h1>",
            unsafe_allow_html=True)
nav = st.sidebar.radio("Navigation", ['Input Section'])

if nav == 'Input Section':

    st.subheader("Please Enter the given values")
    col1, col2 = st.columns(2)
    founded_at = col1.number_input(
        "Founded Year", format="%f")

    first_funding_at = col2.number_input(
        "First Funding Year", format="%f")

    last_funding_at = col1.number_input(
        "Last Funding Year", format="%f")

    funding_rounds = col2.number_input(
        "Funding Rounds", format="%f")

    funding_total_usd = col1.number_input(
        "Total Funding(in US Dollar)", format="%.4f")

    first_milestone_at = col2.number_input(
        "First Milestone Year", format="%f")

    last_milestone_at = col1.number_input(
        "Last Milestone Year", format="%f")

    milestones = col2.number_input(
        "Total Milestones", format="%f")

    if st.button('submit'):
        if -1000.0000 not in ch:

            ch.append(founded_at)
            ch.append(first_funding_at)
            ch.append(last_funding_at)
            ch.append(funding_rounds)
            ch.append(funding_total_usd)
            ch.append(first_milestone_at)
            ch.append(last_milestone_at)
            ch.append(milestones)
            #st.info(f"{ch}")

            #st.info('Submitted')

            val = np.array(ch).reshape(1, -1)
            sc.fit_transform(val)
            val = Predictor(val, qda_model, rf_model)
            st.success(val)

        else:
            st.warning('Input are Empty')

