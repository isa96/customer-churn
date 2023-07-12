import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image



def run() :
    # Membuat Title 
    st.markdown("<h1 style='text-align: center;'>Exploratory Data Analysis</h1>", unsafe_allow_html=True)
    st.write('Berikut adalah EDA dari setiap feature')

    # Import DF
    df_eda = pd.read_csv('eda_churn.csv')

    # Membuat Sub Header
    st.subheader('**EDA Feature Churn**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Customer* yang *churn* lebih banyak dari pada *customer* yang tidak *churn*')

    # Membuat visualisasi Distribusi churn_risk_score
    fig, ax =plt.subplots(1,2,figsize=(15,6))

    sns.countplot(x='churn_risk_score', data=df_eda, palette="winter", ax=ax[0])
    ax[0].set_xlabel("churn_risk_score", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    fig.suptitle('Customer Churn Distribution', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,23000)
    plt.xlabel("churn_risk_score", fontsize= 12)
    plt.ylabel("# of Customer", fontsize= 12)
    ax[0].set_xticks([0,1], ['Not Churn', 'Churn'])
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+405), ha='center', va='center',fontsize = 11) 

    df_eda['churn_risk_score'].value_counts().plot(kind='pie', labels = ['Churn', 'Not Churn'],autopct='%1.1f%%', textprops = {"fontsize":12})
    ax[1].set_ylabel("% of Customer", fontsize= 12)
    st.pyplot(fig)

    # Membuat Sub Header
    st.subheader('**EDA Feature Age**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Customer* paling banyak adalah *customer* yang memiliki *range* umur 40-50 tahun')
    st.markdown('- *Customer* yang paling banyak *churn* adalah *customer* dengan *range* umur 50-60 tahun')
    st.markdown('- Akan tetapi jika dilihat dari persentase *churn* pada setiap kelas *range* umur, maka tidak ada perbedaan signifikan')

    #Visualisasi distribusi range age
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(x='AgeBin', data=df_eda, palette='winter', ax=ax[0])
    ax[0].set_xlabel("Range Customer Age", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    fig.suptitle('Range Customer Age Distribution', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,7600)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+105), ha='center', va='center',fontsize = 10) 

    df_eda['AgeBin'].value_counts().plot(kind='pie', autopct='%1.1f%%', textprops = {"fontsize":12})
    ax[1].set_ylabel("% of Customer", fontsize= 10)
    st.pyplot(fig)

    # Membuat Visualisasi distribusi Age berdasarkan Churn
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(data = df_eda, x = 'AgeBin', hue="churn_risk_score", palette = 'winter', order = ['(10, 20]', '(20, 30]', '(30, 40]', '(40, 50]', '(50, 60]', '(60, 70]'], ax=ax[0])
    ax[0].set_title('Range Age Distribution', fontsize=14, fontweight='bold',)
    ax[0].set_xlabel("Range Age", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    ax[0].tick_params(axis="x", labelsize= 9.5)
    ax[0].legend(fontsize=10,title='Churn Classification', loc='upper right', labels=['Not Churn', 'Churn'])
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+75), ha='center', va='center',fontsize = 10) 
    ax[0].set_ylim(0,4700)

    #Visualisasi % Churn dari setiap kelas
    sns.barplot(x = 'AgeBin', y = 'churn_risk_score', data = df_eda, palette = 'winter', order = ['(10, 20]', '(20, 30]', '(30, 40]', '(40, 50]', '(50, 60]', '(60, 70]'],ax=ax[1])
    ax[1].set_xlabel("Range Age", fontsize= 12)
    ax[1].set_ylabel("% Churn", fontsize= 12)
    ax[1].set_title('% Churn based on Age', fontsize=14, fontweight='bold')
    ax[1].set_ylim(0,0.7)
    for p in ax[1].patches:
        ax[1].annotate("%.2f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+0.03), ha='center', va='center',fontsize = 11) 
    st.pyplot(fig)

    # Membuat Sub Header
    st.subheader('**EDA Feature Time Spent**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- Jika dilihat pada visualisasi diatas maka `avg_time_spent` antara *customer* yang *churn* dan *customer* yang tidak *churn* tidak berbeda secara signifikan')

    #  Visualisasi avg_time_spent vs Churn
    fig =plt.figure(figsize=(15,6))
    plt.rcParams['figure.figsize'] = (10, 5)
    sns.boxenplot(y=df_eda['avg_time_spent'], x= df_eda['churn_risk_score'], palette = 'Blues')
    plt.title('Average Time Spent vs Churn', fontsize = 20)
    st.pyplot(fig)


    # Membuat Sub Header
    st.subheader('**EDA Feature Transaction Value**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Customer* yang tidak *churn* memiliki *average transaction value* yang lebih tinggi (terpusat di 18.000-40.000) dari pada *customer* yang *churn* (terpusat di 16.000-36.000)')

    #  Visualisasi avg_transaction_value vs Churn
    fig =plt.figure(figsize=(15,6))
    plt.rcParams['figure.figsize'] = (10, 5)
    sns.boxenplot(y=df_eda['avg_transaction_value'], x= df_eda['churn_risk_score'], palette = 'Blues')
    plt.title('Average Transaction Value vs Churn', fontsize = 20)
    st.pyplot(fig)

    # Membuat Sub Header
    st.subheader('**EDA Feature Avg Frequency Login Days**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Customer* yang tidak *churn* memiliki *average frequency login days* yang lebih rendah (terpusat di 8-20x) dari pada *customer* yang *churn* (terpusat di 10-25x)')

    #  Visualisasi avg_frequency_login_days vs Churn
    fig =plt.figure(figsize=(15,6))
    plt.rcParams['figure.figsize'] = (10, 5)
    sns.boxenplot(y=df_eda['avg_frequency_login_days'], x= df_eda['churn_risk_score'], palette = 'Blues')
    plt.title('Average Frequency Login Days vs Churn', fontsize = 20)
    st.pyplot(fig)

    # Membuat Sub Header
    st.subheader('**EDA Feature Point Wallet**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Customer* yang tidak *churn* memiliki *points in wallet* yang lebih tinggi (terpusat di 700-800) dari pada *customer* yang *churn* (terpusat di 600-700)')

    #  Visualisasi points_in_wallet vs Churn
    fig =plt.figure(figsize=(15,6))
    plt.rcParams['figure.figsize'] = (10, 5)
    sns.boxenplot(y=df_eda['points_in_wallet'], x= df_eda['churn_risk_score'], palette = 'Blues')
    plt.title('Points in Wallet vs Churn', fontsize = 20)
    st.pyplot(fig)

    # Membuat Sub Header
    st.subheader('**EDA Feature Gender**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Customer* paling banyak adalah *customer* wanita (50.1%). Akan tetapi tidak berbeda signifikan, hanya berbeda 0.2% dari *customer* pria')
    st.markdown('- *Customer* yang paling banyak *churn* adalah *customer* wanita')
    st.markdown('- Akan tetapi jika dilihat dari persentase *churn* pada setiap kelas *gender*, maka tidak ada perbedaan signifikan')

    #Visualisasi distribusi Gender
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(x='gender', data=df_eda, palette='winter', ax=ax[0])
    ax[0].set_xlabel("Gender", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    fig.suptitle('Gender Distribution', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,21000)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+305), ha='center', va='center',fontsize = 10) 
    df_eda['gender'].value_counts().plot(kind='pie', autopct='%1.1f%%', textprops = {"fontsize":12})
    ax[1].set_ylabel("% of Customer", fontsize= 10)
    st.pyplot(fig)

    # Membuat Visualisasi distribusi Gender berdasarkan Churn
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(data = df_eda, x = 'gender', hue="churn_risk_score", palette = 'winter', ax=ax[0])
    ax[0].set_title('Gender Distribution', fontsize=14, fontweight='bold',)
    ax[0].set_xlabel("Gender", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    ax[0].tick_params(axis="x", labelsize= 9.5)
    ax[0].legend(fontsize=10,title='Churn Classification', loc='upper right', labels=['Not Churn', 'Churn'])
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+175), ha='center', va='center',fontsize = 10) 
    ax[0].set_ylim(0,13000)

    #Visualisasi % Churn dari setiap kelas
    sns.barplot(x = 'gender', y = 'churn_risk_score', data = df_eda, palette = 'winter',ax=ax[1])
    ax[1].set_xlabel("Gender", fontsize= 12)
    ax[1].set_ylabel("% Churn", fontsize= 12)
    ax[1].set_title('% Churn based on Gender', fontsize=14, fontweight='bold')
    ax[1].set_ylim(0,0.7)
    for p in ax[1].patches:
        ax[1].annotate("%.2f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+0.02), ha='center', va='center',fontsize = 11) 
    st.pyplot(fig)

    # Membuat Sub Header
    st.subheader('**EDA Feature Region Category**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Customer* paling banyak adalah *customer* yang berasal dari kota (44.8%)')
    st.markdown('- *Customer* yang paling banyak *churn* adalah *customer* yang tinggal di kota')
    st.markdown('- Akan tetapi jika dilihat dari persentase *churn* pada setiap kelas *region*, maka tidak ada perbedaan signifikan')

    #Visualisasi distribusi region_category
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(x='region_category', data=df_eda, palette='winter', ax=ax[0])
    ax[0].set_xlabel("region_category", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    fig.suptitle('Region Category Distribution', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,16000)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+305), ha='center', va='center',fontsize = 10) 
    df_eda['region_category'].value_counts().plot(kind='pie', autopct='%1.1f%%', textprops = {"fontsize":12})
    ax[1].set_ylabel("% of Customer", fontsize= 10)
    st.pyplot(fig)

    # Membuat Visualisasi distribusi region_category berdasarkan Churn
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(data = df_eda, x = 'region_category', hue="churn_risk_score", palette = 'winter', ax=ax[0])
    ax[0].set_title('Region Category Distribution', fontsize=14, fontweight='bold',)
    ax[0].set_xlabel("region_category", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    ax[0].tick_params(axis="x", labelsize= 9.5)
    ax[0].legend(fontsize=10,title='Churn Classification', loc='upper right', labels=['Not Churn', 'Churn'])
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+180), ha='center', va='center',fontsize = 10) 
    ax[0].set_ylim(0,10000)

    #Visualisasi % Churn dari setiap kelas
    sns.barplot(x = 'region_category', y = 'churn_risk_score', data = df_eda, palette = 'winter',ax=ax[1])
    ax[1].set_xlabel("region_category", fontsize= 12)
    ax[1].set_ylabel("% Churn", fontsize= 12)
    ax[1].set_title('% Churn based on Region Category', fontsize=14, fontweight='bold')
    ax[1].set_ylim(0,0.7)
    for p in ax[1].patches:
        ax[1].annotate("%.2f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+0.03), ha='center', va='center',fontsize = 11) 
    st.pyplot(fig)  

    # Membuat Sub Header
    st.subheader('**EDA Feature Membership Category**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Customer* paling banyak adalah *customer* dengan *basic membership* (20.9%) dan *no membership* (20.8%)')
    st.markdown('- *Customer* yang paling banyak *churn* adalah *customer* dengan *no membership*')
    st.markdown('- Akan tetapi jika dilihat dari persentase *churn* pada setiap kelas *membership*, maka terdapat perbedaan yang signifikan')

    # Visualisasi distribusi membership_category
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(x='membership_category', data=df_eda, palette='winter', ax=ax[0])
    ax[0].set_xlabel("membership_category", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    fig.suptitle('Membership Category Distribution', fontsize=18, fontweight='bold')
    ax[0].tick_params(axis='x', rotation=90)
    ax[0].set_ylim(0,8500)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+185), ha='center', va='center',fontsize = 10) 

    df_eda['membership_category'].value_counts().plot(kind='pie', autopct='%1.1f%%', textprops = {"fontsize":12})
    ax[1].set_ylabel("% of Customer", fontsize= 10)
    st.pyplot(fig)
    # Membuat Visualisasi distribusi membership_category berdasarkan Churn
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(data = df_eda, x = 'membership_category', hue="churn_risk_score", palette = 'winter', ax=ax[0])
    ax[0].set_title('Membership Category Distribution', fontsize=14, fontweight='bold',)
    ax[0].set_xlabel("membership_category", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    ax[0].tick_params(axis="x", labelsize= 9.5)
    ax[0].legend(fontsize=10,title='Churn Classification', loc='upper right', labels=['Not Churn', 'Churn'])
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+180), ha='center', va='center',fontsize = 10) 
    ax[0].tick_params(axis='x', rotation=90)
    ax[0].set_ylim(0,8500)

    #Visualisasi % Churn dari setiap kelas
    sns.barplot(x = 'membership_category', y = 'churn_risk_score', data = df_eda, palette = 'winter',ax=ax[1])
    ax[1].set_xlabel("membership_category", fontsize= 12)
    ax[1].set_ylabel("% Churn", fontsize= 12)
    ax[1].set_title('% Churn based on Membership Category', fontsize=14, fontweight='bold')
    ax[1].set_ylim(0,1.2)
    ax[1].tick_params(axis='x', rotation=90)
    for p in ax[1].patches:
        ax[1].annotate("%.2f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+0.03), ha='center', va='center',fontsize = 11) 

    st.pyplot(fig)

    st.subheader('**EDA Feature Joined Through Referral**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Customer* paling banyak adalah *customer* yang tidak menggunakan *referral* (50.2%). Akan tetapi tidak berbeda signifikan, hanya berbeda 0.4% dari *customer* yang menggunakan *referral*')
    st.markdown('- *Customer* yang paling banyak *churn* adalah *customer* dengan *referral*')
    st.markdown('- Akan tetapi jika dilihat dari persentase *churn* pada setiap kelas *joined through referral*, maka tidak terdapat perbedaan yang signifikan')

    # Visualisasi distribusi joined_through_referral
    fig, ax =plt.subplots(1,2,figsize=(15,6))

    sns.countplot(x='joined_through_referral', data=df_eda, palette='winter', ax=ax[0])
    ax[0].set_xlabel("joined_through_referral", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    fig.suptitle('Joined Through Referral Distribution', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,17500)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+235), ha='center', va='center',fontsize = 10) 

    df_eda['joined_through_referral'].value_counts().plot(kind='pie', autopct='%1.1f%%', textprops = {"fontsize":12})
    ax[1].set_ylabel("% of Customer", fontsize= 10)
    st.pyplot(fig)

    # Membuat Visualisasi distribusi joined_through_referral berdasarkan Churn
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(data = df_eda, x = 'joined_through_referral', hue="churn_risk_score", palette = 'winter', ax=ax[0])
    ax[0].set_title('Joined Through Referral Distribution', fontsize=14, fontweight='bold',)
    ax[0].set_xlabel("joined_through_referral", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    ax[0].tick_params(axis="x", labelsize= 9.5)
    ax[0].legend(fontsize=10,title='Churn Classification', loc='upper right', labels=['Not Churn', 'Churn'])
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+180), ha='center', va='center',fontsize = 10) 
    ax[0].set_ylim(0,12000)

    #Visualisasi % Churn dari setiap kelas
    sns.barplot(x = 'joined_through_referral', y = 'churn_risk_score', data = df_eda, palette = 'winter',ax=ax[1])
    ax[1].set_xlabel("joined_through_referral", fontsize= 12)
    ax[1].set_ylabel("% Churn", fontsize= 12)
    ax[1].set_title('% Churn based on Joined Through Referral', fontsize=14, fontweight='bold')
    ax[1].set_ylim(0,0.8)
    for p in ax[1].patches:
        ax[1].annotate("%.2f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+0.03), ha='center', va='center',fontsize = 11) 

    st.pyplot(fig)

    st.subheader('**EDA Feature Preferred Offer Types**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Customer* paling banyak adalah *customer* menggunakan kupon (33.7%)')
    st.markdown('- *Customer* yang paling banyak *churn* adalah *customer* yang tidak menggunakan penawaran')
    st.markdown('- Akan tetapi jika dilihat dari persentase *churn* pada setiap kelas *preferred offer types*, maka tidak terdapat perbedaan yang signifikan')

    #Visualisasi distribusi preferred_offer_types
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(x='preferred_offer_types', data=df_eda, palette='winter', ax=ax[0])
    ax[0].set_xlabel("preferred_offer_types", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    fig.suptitle('Offer Types Distribution', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,14000)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+235), ha='center', va='center',fontsize = 10) 

    df_eda['preferred_offer_types'].value_counts().plot(kind='pie', autopct='%1.1f%%', textprops = {"fontsize":10})
    ax[1].set_ylabel("% of Customer", fontsize= 10)
    st.pyplot(fig)

    # Membuat Visualisasi distribusi preferred_offer_types berdasarkan Churn
    fig, ax =plt.subplots(1,2,figsize=(15,6))

    sns.countplot(data = df_eda, x = 'preferred_offer_types', hue="churn_risk_score", palette = 'winter', ax=ax[0])
    ax[0].set_title('Offer Types Distribution', fontsize=14, fontweight='bold',)
    ax[0].set_xlabel("preferred_offer_types", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    ax[0].tick_params(axis="x", labelsize= 9.5)
    ax[0].legend(fontsize=10,title='Churn Classification', loc='upper right', labels=['Not Churn', 'Churn'])
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+180), ha='center', va='center',fontsize = 10) 
    ax[0].set_ylim(0,9000)

    #Visualisasi % Churn dari setiap kelas
    sns.barplot(x = 'preferred_offer_types', y = 'churn_risk_score', data = df_eda, palette = 'winter',ax=ax[1])
    ax[1].set_xlabel("preferred_offer_types", fontsize= 12)
    ax[1].set_ylabel("% Churn", fontsize= 12)
    ax[1].set_title('% Churn based on Offer Types', fontsize=14, fontweight='bold')
    ax[1].set_ylim(0,0.8)
    for p in ax[1].patches:
        ax[1].annotate("%.2f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+0.03), ha='center', va='center',fontsize = 11) 

    st.pyplot(fig)

    st.subheader('**EDA Feature Used Special Discount Types**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Customer* paling banyak adalah *customer* yang menggunakan diskon (55%)')
    st.markdown('- *Customer* yang paling banyak *churn* adalah *customer* yang menggunakan diskon')
    st.markdown('- Akan tetapi jika dilihat dari persentase *churn* pada setiap kelas *used special discount*, maka tidak terdapat perbedaan yang signifikan')

    #Visualisasi distribusi used_special_discount
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(x='used_special_discount', data=df_eda, palette='winter', ax=ax[0])
    ax[0].set_xlabel("used_special_discount", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    fig.suptitle('Used Special Discount Distribution', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,23000)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+335), ha='center', va='center',fontsize = 10) 

    df_eda['used_special_discount'].value_counts().plot(kind='pie', autopct='%1.1f%%', textprops = {"fontsize":10})
    ax[1].set_ylabel("% of Customer", fontsize= 10)
    st.pyplot(fig)

    # Membuat Visualisasi distribusi used_special_discount berdasarkan Churn
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(data = df_eda, x = 'used_special_discount', hue="churn_risk_score", palette = 'winter', ax=ax[0])
    ax[0].set_title('Used Special Discount Distribution', fontsize=14, fontweight='bold',)
    ax[0].set_xlabel("used_special_discount", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    ax[0].tick_params(axis="x", labelsize= 9.5)
    ax[0].legend(fontsize=10,title='Churn Classification', loc='upper right', labels=['Not Churn', 'Churn'])
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+180), ha='center', va='center',fontsize = 10) 
    ax[0].set_ylim(0,12000)

    #Visualisasi % Churn dari setiap kelas
    sns.barplot(x = 'used_special_discount', y = 'churn_risk_score', data = df_eda, palette = 'winter', ax=ax[1])
    ax[1].set_xlabel("used_special_discount", fontsize= 12)
    ax[1].set_ylabel("% Churn", fontsize= 12)
    ax[1].set_title('% Churn based on Used Special Discount', fontsize=14, fontweight='bold')
    ax[1].set_ylim(0,0.8)
    for p in ax[1].patches:
        ax[1].annotate("%.2f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+0.03), ha='center', va='center',fontsize = 11) 

    st.pyplot(fig)

    st.subheader('**EDA Feature Offer Application Preference**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Customer* paling banyak adalah *customer* yang menyukai tawaran (55.3%)')
    st.markdown('- *Customer* yang paling banyak *churn* adalah *customer* yang menyukai tawaran')
    st.markdown('- Akan tetapi jika dilihat dari persentase *churn* pada setiap kelas kelas tawaran, maka tidak terdapat perbedaan yang signifikan')

    #Visualisasi distribusi offer_application_preference
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(x='offer_application_preference', data=df_eda, palette='winter', ax=ax[0])
    ax[0].set_xlabel("offer_application_preference", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    fig.suptitle('Offer Aplication Preference Distribution', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,23000)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+335), ha='center', va='center',fontsize = 10) 

    df_eda['offer_application_preference'].value_counts().plot(kind='pie', autopct='%1.1f%%', textprops = {"fontsize":10})
    ax[1].set_ylabel("% of Customer", fontsize= 10)
    st.pyplot(fig)

    # Membuat Visualisasi distribusi offer_application_preference berdasarkan Churn
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(data = df_eda, x = 'offer_application_preference', hue="churn_risk_score", palette = 'winter', ax=ax[0])
    ax[0].set_title('Offer Aplication Preference Distribution', fontsize=14, fontweight='bold',)
    ax[0].set_xlabel("offer_application_preference", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    ax[0].tick_params(axis="x", labelsize= 9.5)
    ax[0].legend(fontsize=10,title='Churn Classification', loc='upper right', labels=['Not Churn', 'Churn'])
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+180), ha='center', va='center',fontsize = 10) 
    ax[0].set_ylim(0,12000)

    #Visualisasi % Churn dari setiap kelas
    sns.barplot(x = 'offer_application_preference', y = 'churn_risk_score', data = df_eda, palette = 'winter',ax=ax[1])
    ax[1].set_xlabel("offer_application_preference", fontsize= 12)
    ax[1].set_ylabel("% Churn", fontsize= 12)
    ax[1].set_title('% Churn based on Offer Aplication Preference', fontsize=14, fontweight='bold')
    ax[1].set_ylim(0,0.8)
    for p in ax[1].patches:
        ax[1].annotate("%.2f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+0.03), ha='center', va='center',fontsize = 11) 
    st.pyplot(fig)

    st.subheader('**EDA Feature Past Complaint**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Customer* paling banyak adalah *customer* yang tidak *complaint* (50.3%). Akan tetapi tidak berbeda signifikan, hanya berbeda 0.6% dari *customer* yang *complaint*')
    st.markdown('- *Customer* yang paling banyak *churn* adalah *customer* yang *complaint*')
    st.markdown('- Akan tetapi jika dilihat dari persentase *churn* pada setiap kelas *past complaint*, maka tidak terdapat perbedaan yang signifikan')

    #Visualisasi distribusi past_complaint
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(x='past_complaint', data=df_eda, palette='winter', ax=ax[0])
    ax[0].set_xlabel("past_complaint", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    fig.suptitle('Past Complaint Distribution', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,23000)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+335), ha='center', va='center',fontsize = 10) 
    df_eda['past_complaint'].value_counts().plot(kind='pie', autopct='%1.1f%%', textprops = {"fontsize":10})
    ax[1].set_ylabel("% of Customer", fontsize= 10)
    st.pyplot(fig)

    # Membuat Visualisasi distribusi past_complaint berdasarkan Churn
    fig, ax =plt.subplots(1,2,figsize=(15,6))

    sns.countplot(data = df_eda, x = 'past_complaint', hue="churn_risk_score", palette = 'winter', ax=ax[0])
    ax[0].set_title('Past Complaint Distribution', fontsize=14, fontweight='bold',)
    ax[0].set_xlabel("past_complaint", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    ax[0].tick_params(axis="x", labelsize= 9.5)
    ax[0].legend(fontsize=10,title='Churn Classification', loc='upper right', labels=['Not Churn', 'Churn'])
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+180), ha='center', va='center',fontsize = 10) 
    ax[0].set_ylim(0,14000)

    #Visualisasi % Churn dari setiap kelas
    sns.barplot(x = 'past_complaint', y = 'churn_risk_score', data = df_eda, palette = 'winter', ax=ax[1])
    ax[1].set_xlabel("past_complaint", fontsize= 12)
    ax[1].set_ylabel("% Churn", fontsize= 12)
    ax[1].set_title('% Churn based on Past Complaint', fontsize=14, fontweight='bold')
    ax[1].set_ylim(0,0.8)
    for p in ax[1].patches:
        ax[1].annotate("%.2f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+0.03), ha='center', va='center',fontsize = 11) 

    st.pyplot(fig)

    st.subheader('**EDA Feature Complaint Status**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Customer* paling banyak adalah *customer* yang *complaint* nya tidak dapat diaplikasikan/direalisasikan (50.3%)')
    st.markdown('- *Customer* yang paling banyak *churn* adalah *customer* yang *complaint* nya tidak dapat diaplikasikan/direalisasikan')
    st.markdown('- Akan tetapi jika dilihat dari persentase *churn* pada setiap kelas *complaint status*, maka tidak terdapat perbedaan yang signifikan')

    #Visualisasi distribusi complaint_status
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(x='complaint_status', data=df_eda, palette='winter', ax=ax[0])
    ax[0].set_xlabel("complaint_status", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    fig.suptitle('Complaint Status Distribution', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,23000)
    ax[0].tick_params(axis='x', rotation=90)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+335), ha='center', va='center',fontsize = 10) 

    df_eda['complaint_status'].value_counts().plot(kind='pie', autopct='%1.1f%%', textprops = {"fontsize":10})
    ax[1].set_ylabel("% of Customer", fontsize= 10)
    st.pyplot(fig)

    # Membuat Visualisasi distribusi complaint_status berdasarkan Churn
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(data = df_eda, x = 'complaint_status', hue="churn_risk_score", palette = 'winter', ax=ax[0])
    ax[0].set_title('Complaint Status Distribution', fontsize=14, fontweight='bold',)
    ax[0].set_xlabel("complaint_status", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    ax[0].tick_params(axis="x", labelsize= 9.5)
    ax[0].legend(fontsize=10,title='Churn Classification', loc='upper right', labels=['Not Churn', 'Churn'])
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+180), ha='center', va='center',fontsize = 10)
    ax[0].tick_params(axis='x', rotation=90)
    ax[0].set_ylim(0,12000)

    #Visualisasi % Churn dari setiap kelas
    sns.barplot(x = 'complaint_status', y = 'churn_risk_score', data = df_eda, palette = 'winter',ax=ax[1])
    ax[1].set_xlabel("complaint_status", fontsize= 12)
    ax[1].set_ylabel("% Churn", fontsize= 12)
    ax[1].set_title('% Churn based on Complaint Status', fontsize=14, fontweight='bold')
    ax[1].set_ylim(0,0.8)
    ax[1].tick_params(axis='x', rotation=90)
    for p in ax[1].patches:
        ax[1].annotate("%.2f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+0.03), ha='center', va='center',fontsize = 11) 

    st.pyplot(fig)

    st.subheader('**EDA Feature Feedback**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Customer* paling banyak adalah *customer* yang memberikan *feedback* buruk (*too many ads*, *poor product quality*) dan yang tidak memberikan *feedback*. 3 kelas tersebut memiliki persentase proporsi 17%')
    st.markdown('- *Customer* yang paling banyak *churn* adalah *customer* yang memberikan *feedback poor product quality*')
    st.markdown('- Akan tetapi jika dilihat dari persentase *churn* pada setiap kelas *feedback*, maka terdapat perbedaan yang signifikan')

    # Visualisasi distribusi feedback
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(x='feedback', data=df_eda, palette='winter', ax=ax[0])
    ax[0].set_xlabel("feedback", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    fig.suptitle('Feedback Distribution', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,7000)
    ax[0].tick_params(axis='x', rotation=90)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+135), ha='center', va='center',fontsize = 10) 
    df_eda['feedback'].value_counts().plot(kind='pie', autopct='%1.1f%%', textprops = {"fontsize":10})
    ax[1].set_ylabel("% of Customer", fontsize= 10)
    st.pyplot(fig)

    # Membuat Visualisasi distribusi feedback berdasarkan Churn
    fig, ax =plt.subplots(1,2,figsize=(15,6))
    sns.countplot(data = df_eda, x = 'feedback', hue="churn_risk_score", palette = 'winter', ax=ax[0])
    ax[0].set_title('Feedback Distribution', fontsize=14, fontweight='bold',)
    ax[0].set_xlabel("feedback", fontsize= 12)
    ax[0].set_ylabel("# of Customer", fontsize= 12)
    ax[0].tick_params(axis="x", labelsize= 9.5)
    ax[0].legend(fontsize=10,title='Churn Classification', loc='upper right', labels=['Not Churn', 'Churn'])
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+60), ha='center', va='center',fontsize = 6)
    ax[0].tick_params(axis='x', rotation=90)
    ax[0].set_ylim(0,5000)

    #Visualisasi % Churn dari setiap kelas
    sns.barplot(x = 'feedback', y = 'churn_risk_score', data = df_eda, palette = 'winter',ax=ax[1])
    ax[1].set_xlabel("feedback", fontsize= 12)
    ax[1].set_ylabel("% Churn", fontsize= 12)
    ax[1].set_title('% Churn based on Feedback', fontsize=14, fontweight='bold')
    ax[1].set_ylim(0,0.8)
    ax[1].tick_params(axis='x', rotation=90)
    for p in ax[1].patches:
        ax[1].annotate("%.2f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+0.03), ha='center', va='center',fontsize = 11) 
    st.pyplot(fig)


if __name__ == '__main__':
    run()