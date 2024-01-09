import pickle
import streamlit as st 
Heart_disease_prediction=pickle.load(open('C:/Heart disease prediction'))
st.title('Heart disease prediction Using ML')
col1, col2, col3 = st.columns(3)
with col1:
    Age=st.text_input('Age')
with col2:
    Sex=st.text_input('Sex')
with col3:
    col=st.text_input('col')
with col1:
    trestbps=st.text_input('trestbps')
with col2:
    fbs=st.text_input('fbs')
with col3:
    thal=st.text_input('thal')
Heart_disease_prediction=''
if st.button('Heart disease prediction'):
    if ('target==1'):
        Heart_disease_prediction='Heart Patient'
    else:
        Heart_disease_prediction='Not a Heart Patient'
st.success(Heart_disease_prediction)
        
