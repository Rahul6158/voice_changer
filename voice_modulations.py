import streamlit as st
from googletrans import Translator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Function to remove stopwords from text
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_text = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_text)

# Function to translate text to the target language
def translate_text(text, target_language='fr'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Streamlit app
st.title('Text Processing and Translation App')

# Input text area
input_text = st.text_area('Enter your text here:')

# Select target language
target_language = st.selectbox('Select target language:', ['fr', 'es', 'de', 'it', 'ja', 'ko', 'zh-CN'])

# Button to process and translate text
if st.button('Process and Translate'):
    cleaned_text = remove_stopwords(input_text)
    translated_text = translate_text(cleaned_text, target_language=target_language)
    
    # Display cleaned and translated text
    st.write('Cleaned Text:', cleaned_text)
    st.write('Translated Text:', translated_text)
