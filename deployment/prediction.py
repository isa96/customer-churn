import streamlit as st
import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model


def run() :
  # Load Model
  with open('preprocessor.pkl', 'rb') as file_1:
    preprocessor = pickle.load(file_1)
  model_churn = load_model('churn_model.h5', compile=False)

  # Membuat Title 
  st.markdown("<h1 style='text-align: center;'>Churn Prediction</h1>", unsafe_allow_html=True)

  # Menambahkan Deskripsi Form
  st.write('Page ini berisi model untuk memprediksi churn customer')

  #Membuat Form
  with st.form(key= 'form_customer'):
      
      st.markdown('### **Customer Data**')
      user_id = st.text_input('User ID',value= '')
      age = st.slider('Age',10,70,30)
      gender = st.selectbox('Gender',('M','F'),index=1)
      region_category = st.radio('Region', options=['City','Village','Town'], horizontal=True)
      internet_option = st.selectbox('Internet Option',('Wi-Fi','Fiber_Optic', 'Mobile_Data'),index=1)
      medium_of_operation = st.radio('Medium', options=['Desktop','Smartphone','Both'], horizontal=True)
      st.markdown('---')
      st.markdown('### **Login Data**')
      days_since_last_login = st.slider('Days Since Last Login',0,30,3)
      avg_frequency_login_days = st.slider('Avg Frequency Login Days',0,73,14)
      st.markdown('---')
      st.markdown('### **Membership Data**')
      joined_through_referral = st.selectbox('Referral',('Yes','No'),index=1)
      membership_category = st.selectbox('Membership Category',('No Membership','Basic Membership','Silver Membership', 'Premium Membership', 'Gold Membership', 'Platinum Membership'),index=1)
      st.markdown('---')
      st.markdown('### **Transaction Data**')
      points_in_wallet = st.number_input('Points in Wallet', min_value=0, max_value=2070, value=600 ,step=1)
      avg_transaction_value = st.number_input('Avg Transaction Value', min_value=800, max_value=90000, value=30000 ,step=1)
      preferred_offer_types = st.radio('Offer Types', options=['Without Offers','Credit/Debit Card Offers','Gift Vouchers/Coupons'], horizontal=True)
      used_special_discount = st.selectbox('Used Special Discount',('Yes','No'),index=1)
      past_complaint = st.selectbox('Past Complaint',('Yes','No'),index=1)
      feedback = st.selectbox('Feedback',('Poor Website','Poor Customer Service', 'Too many ads', 'Poor Product Quality', 'No reason specified', 'Products always in Stock', 'Reasonable Price', 'Quality Customer Care', 'User Friendly Website'),index=1)
      submitted = st.form_submit_button('Predict')

  # Create New Data 
  data_inf = {
      'user_id' : user_id,
      'age' : age,
      'gender' : gender,
      'region_category' : region_category,
      'internet_option' : internet_option, 
      'medium_of_operation' : medium_of_operation,
      'days_since_last_login' : days_since_last_login, 
      'avg_frequency_login_days' : avg_frequency_login_days, 
      'joined_through_referral' : joined_through_referral,
      'membership_category' : membership_category,  
      'points_in_wallet' : points_in_wallet, 
      'avg_transaction_value' : avg_transaction_value,  
      'used_special_discount' : used_special_discount,
      'past_complaint' : past_complaint, 
      'preferred_offer_types' : preferred_offer_types,                
      'feedback' : feedback                                   
  }

  data_inf = pd.DataFrame([data_inf])
  data_inf

  if submitted :
    # Feature Scaling and Feature Encoding
    data_final = preprocessor.transform(data_inf)

    # Predict using Linear Regression
    y_inf_pred = np.where(model_churn.predict(data_final) >= 0.5, 1, 0)
    
    if y_inf_pred == 1:
      prediction = 'Churn'
    else:
      prediction = 'Not Churn'

    st.write('# Churn Prediction : ', prediction)

if __name__ == '__main__':
    run()