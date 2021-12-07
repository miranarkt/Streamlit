# Import des modules
import streamlit as st
import pandas as pd
import plotly.express as px 
from PIL import Image

# Utilise tout l'espace disponible
st.set_page_config(layout='wide')

# Titre du Dashboard
st.title("#WebFruitSummer - Cible 🍋🫐")

# Organisation du dashboard 
left_block, right_block = st.columns([1, 1])

# Chargement des données
df = pd.read_excel('https://github.com/miranarkt/Streamlit/blob/master/marketing_campaign_2.xls', sheet_name='marketing_campaign_2')

#Transformer les données
del df['Complain']
#st.dataframe(df)

# Création d'un nouveau JDD
df2 = df.copy() 
df2.reset_index(inplace=True)
#st.dataframe(df2)

#Calculer l'âge à partir de l'année de naissance
age = []
for i in df2['Year_Birth']:
    age.append(2021 - i)

df2['Age'] = age

#### PREMIER GRAPHIQUE ####

#Regroupement des achats en ligne par âge 

NumWebPurchases_per_age = df2[['Age', 'NumWebPurchases']].groupby('Age', as_index=False).agg('sum').sort_values(by='NumWebPurchases', ascending=False)
#st.write(NumWebPurchases_per_year_birth)

with left_block:
    st.subheader('Définition de la cible')
    first_container = st.container()
    with first_container: 
        fig = px.bar(NumWebPurchases_per_age[:50], \
                    x='Age', \
                    y='NumWebPurchases', \
                    text='NumWebPurchases', \
                    title='Nombre d\'achats en ligne en fonction de l\'âge', \
                    labels={'NumWebPurchases': 'Achats en ligne', 'Age': 'Âge'},
                    color='Age',
                    color_continuous_scale='Agsunset',
                    barmode='group')  
        fig.update_layout(plot_bgcolor='white')
        fig.update_layout(width=1300,height=500)
        fig.update_layout(
        font_color='black',
        font_family='Quicksand',
        font_size=15,
        title_font_color='rgb(44, 5, 148, 255)',
        title_font_size=25,
        title_font_family='Quicksand',
        legend_title_font_color='red',
        legend_title_font_size=15,
        legend_title_font_family='Quicksand')
        st.plotly_chart(fig)



#### DEUXIEME GRAPH ####

col1, col2 = st.columns(2)

#Regroupement des achats en promotion par nombre d'enfants

deal_purchases_per_kidhome = df2[['Kidhome', 'NumDealsPurchases']].groupby(by=['Kidhome'], as_index=False).agg('count')
#st.write(income_per_kidhome)

with col1:
    container_1 = st.container()
    with container_1:
        st.write('#')
    container_2 = st.container()
    with container_2:
        st.write('#')
    container_3 = st.container()
    with container_3:
        st.write('#')
    container_4 = st.container()
    with container_4:
        st.write('') 
    
    number_purchase_discount = st.container()
    with number_purchase_discount: 
        fig2 = px.line(deal_purchases_per_kidhome,
        x="Kidhome",
        y="NumDealsPurchases",
        title='Nombre d\'achats avec promotion en fonction du nombre d\'enfants',
        labels={'NumDealsPurchases': 'Achats avec promotion', 'Kidhome':'Nombre d\'enfants'})
        fig2.update_traces(mode='lines+markers')
        fig2.update_layout(
        font_color='black',
        font_family='Quicksand',
        font_size=15,
        title_font_color='rgb(44, 5, 148, 255)',
        title_font_size=19,
        title_font_family='Quicksand',
        legend_title_font_color='red',
        legend_title_font_size=15,
        legend_title_font_family='Quicksand')
        st.plotly_chart(fig2)

#### TROISIEME GRAPH ####

with col2:
    bouton_select = st.container()
    with bouton_select:
        bouton_marital_status = st.multiselect(
        label='Choisir le statut marital',
        options=df2['Marital_Status'].unique(),
        default=['Married', 'Together', 'Single', 'Divorced', 'Widow', 'Alone', 'Absurd', 'YOLO'])
    
    with number_purchase_discount: 
     #Regroupement des achats en promotion par statut marital  
     web_purchase_per_marital_status = df2[['Marital_Status', 'NumDealsPurchases', 'NumWebPurchases']].groupby(by=['Marital_Status'], as_index=False).agg('count').sort_values(by='NumDealsPurchases', ascending=True)
     web_purchase_per_marital_status = web_purchase_per_marital_status.query('Marital_Status in @bouton_marital_status')
    
    fig5 = px.bar(web_purchase_per_marital_status,
    x="NumDealsPurchases",
    y="Marital_Status",
    color='NumWebPurchases',
    orientation='h',
    color_continuous_scale='Agsunset',
    title='Nombre d\'achats avec promotion en fonction du statut marital',
    labels={'NumDealsPurchases': 'Achats avec promotion', 'Marital_Status':'Statut marital'})
    fig5.update_layout(plot_bgcolor='white')
    fig5.update_layout(width=700,height=500)
    fig5.update_layout(
        font_color='black',
        font_family='Quicksand',
        font_size=15,
        title_font_color='rgb(44, 5, 148, 255)',
        title_font_size=19,
        title_font_family='Quicksand',
        legend_title_font_color='red',
        legend_title_font_size=15,
        legend_title_font_family='Quicksand')

    st.plotly_chart(fig5)

#### QUATRIEME GRAPH ####

#Regroupement de la fréquence d'achat pour les personnes mariées

product_choice = df2[['Marital_Status','Frequency']].groupby(by=['Marital_Status'], as_index=False).count()
#st.write(product_choice)

fig3 = px.pie(df2.query("Marital_Status == 'Married'").round(),
values='Frequency',
names='Frequency',
title='Fréquentation par semaine des personnes mariées',
labels={'Frequency': 'Nombre de jours de visite', 'Marital_Status':'Statut marital'},
color_discrete_sequence=px.colors.sequential.Agsunset
)
fig3.update_traces(textposition='inside', textinfo='percent+label')
fig5.update_layout(plot_bgcolor='white')
fig5.update_layout(width=700,height=500)
fig3.update_layout(
font_color='black',
font_family='Quicksand',
font_size=15,
title_font_color='rgb(44, 5, 148, 255)',
title_font_size=19,
title_font_family='Quicksand',
legend_title_font_color='red',
legend_title_font_size=15,
legend_title_font_family='Quicksand')
st.plotly_chart(fig3)

# Téléchargement de mon dataset 

@st.cache
def convert_df(df):
     return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="Télécharger mon dataset",
     data=csv,
     file_name='dataset_mirana.csv',
     mime='text/csv',
 )

# Bannière de fin

image = Image.open('banner.png')
st.image(image, use_column_width='always')

