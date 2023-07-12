import streamlit as st
import eda
import prediction

# Set Config dan icon
st.set_page_config(
        page_title='Churn Prediction',
        layout='wide',
        )

# Hide Streamlit Style
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

#Membuat navigasi
navigation = st.sidebar.selectbox('Pilih Halaman (Churn Prediction/EDA): ', ('Churn Prediction','Exploratory Data Analysis'))
st.sidebar.image("https://imgur.com/t4aS0jH.png", use_column_width=True)

#Run modul dengan if else
if navigation == 'Churn Prediction' :
    prediction.run()
else :
    eda.run()