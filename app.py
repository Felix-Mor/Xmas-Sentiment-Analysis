import streamlit as st
import pandas as pd
df = pd.read_csv('sentiment.csv')
sent_df = df[['year','anger', 'anticipation','disgust', 'fear', 'joy','negative', 'positive', 'sadness', 'surprise', 'trust' ]].set_index('year')
st.title('Christmas Speech Sentiment Analysis')
st.text('Pick an emotion/emotions and see the corrensponding scores for each Royal Christmas Speech from 1997-2022')
columns = st.multiselect(
    'Pick some emotions',
    ['anger', 'anticipation','disgust', 'fear', 'joy','negative', 'positive', 'sadness', 'surprise', 'trust' ],
    ['trust', 'fear'])
st.line_chart(sent_df[columns])
st.text('You can change the order to ascending or descending in this \
    table by clicking on a column title.')
sent_df[columns]
