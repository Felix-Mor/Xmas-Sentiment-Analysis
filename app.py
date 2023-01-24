import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
df = pd.read_csv('sentiment.csv')
sent_df = df[['year','anger', 'anticipation','disgust', 'fear', 'joy','negative', 'positive', 'sadness', 'surprise', 'trust' ]].set_index('year')
st.title('Christmas Speech Sentiment Analysis')
st.write('The following analysis of the Royal Christmas Speeches 1997-2022 was completed using the NRC Lexicon to generate a score for a series of emotions. Select some emotions from the drop down menu to see the corresponding scores by year on the graph below.')
columns = st.multiselect(
    'Pick some emotions',
    ['anger', 'anticipation','disgust', 'fear', 'joy','negative', 'positive', 'sadness', 'surprise', 'trust' ],
    ['trust', 'fear'])
st.line_chart(sent_df[columns], use_container_width=True)
# st.text('Click on column title to change order')
# sent_df
st.subheader('Pick a year to see a wordcloud')
yr = st.slider('Slide to select', min_value= 1997, max_value= 2022)
inp = int(yr)
df1 = df.set_index('year')
df1 = df1['text']
text = df1[inp]
stopwords = set(STOPWORDS)
stopwords.update(["one", "us", 'year', 'years, ','many', 'whatever', 'know', 'much', 'every', 'day', 'today', 'will', 's'])

wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
st.set_option('deprecation.showPyplotGlobalUse', False)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
fig = plt.show()
st.pyplot(fig)
