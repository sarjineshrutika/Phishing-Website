import streamlit as st
import pandas as pd
import joblib
import numpy as np

model= joblib.load('best_model')

st.header('Phishing Website  Prediction App')

 # x[['ip', 'nb_qm', 'nb_www', 'ratio_digits_url', 'phish_hints',
  #     'nb_hyperlinks', 'domain_in_title', 'domain_age', 'google_index',
   #    'page_rank']]
ip = st.number_input("enter ip")
nb_qm= st.number_input("enter nb_qm")
nb_www=st.number_input("enter nb_www")
ratio_digits_url=st.number_input("enter ratio_digits_url")
phish_hints=st.number_input("enter phish_hints")
nb_hyperlinks=st.number_input("enter nb_hyperlinks")
domain_int_title=st.number_input("enter domain_in_title")
domain_age=st.number_input("enter domain_age")
google_index=st.number_input("enter google_index")
page_rank=st.number_input("enter page_rank")
df= pd.DataFrame([{'ip' : ip,
                   'nb_qm': nb_qm,
                   'nb_www' : nb_www,
                   'ratio_digits_url' : ratio_digits_url,
                   'phish_hints' : phish_hints,
                   'nb_hyperlinks': nb_hyperlinks,
                   'domain_in_title': domain_int_title,
                   'domain_age' : domain_age,
                   'google_index' : google_index,
                   'page_rank' : page_rank}])

st.write(df)


pred =model.predict(df)

submit=st.button("Enter to see the prediction")
if submit:
    st.subheader("The predicted status is..")
    st.write(pred)