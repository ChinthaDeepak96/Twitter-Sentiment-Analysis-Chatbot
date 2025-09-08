import streamlit as st
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('stopwords')
nltk.download('wordnet')

model = tf.keras.models.load_model('sentiment_model.h5')
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = text.split()

    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

def run_streamlit_app():
    st.title("Twitter Sentiment Analysis Chatbot")
    user_input = st.text_area("Enter your tweet here:")
    if st.button("Analyze Sentiment"):
        processed_input = preprocess_text(user_input)
        sequence = tokenizer.texts_to_sequences([processed_input])
        padded_sequence = pad_sequences(sequence, maxlen=50)
        prediction = model.predict(padded_sequence)[0][0]

        sentiment = "Positive" if prediction > 0.5 else "Negative"
        confidence = prediction if prediction > 0.5 else 1 - prediction
        st.write(f"Sentiment: {sentiment}")
        st.write(f"Confidence: {confidence:.2f}")
    else:
        st.write("Please enter a tweet to analyze.")

if __name__ == "__main__":
    run_streamlit_app()



# FOR OUTPUT

#pip install streamlit tensorflow nltk

#python -m nltk.downloader stopwords
#python -m nltk.downloader wordnet

#streamlit run main_nlp_file.py