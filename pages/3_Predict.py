import streamlit as st
import joblib
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from autocorrect import Speller
from emoji import demojize
from contractions import fix
from textacy.preprocessing.remove import accents
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from sklearn.linear_model import SGDClassifier

st.markdown(
    """
    <style>
        body {
            background-color: #002b36;
            color: white;
        }
        .stButton>button {
            background-color: #FF4B4B;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Load saved components
lr = joblib.load('tag_predictor.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')
mlb_classes = joblib.load('mlb_classes.pkl')

# Initialize preprocessing tools
speller = Speller()
stopword = stopwords.words("english")
stem = SnowballStemmer("english")
lem = WordNetLemmatizer()

# Text preprocessing function
def text_pre_processing(text):
    text = re.sub(r"[^a-z0-9]", " ", text.lower())  # Normalize case & remove punctuation
    words = word_tokenize(text)
    new_text = [lem.lemmatize(stem.stem(word)) for word in words if word not in stopword]
    return " ".join(new_text)

# Prediction function
def predict_tags(text, model=lr, threshold=0.5):
    clean_text = text_pre_processing(text)
    text_tfidf = tfidf.transform([clean_text])
    
    if hasattr(model, 'predict_proba'):
        probas = model.predict_proba(text_tfidf)
        tags = [mlb_classes[i] for i, class_name in enumerate(mlb_classes) if probas[i][0][1] > threshold]
    else:
        preds = model.predict(text_tfidf)
        tags = [mlb_classes[i] for i, val in enumerate(preds[0]) if val == 1]
    
    return tags

# Streamlit UI Enhancements
st.markdown("""
    <style>
        /* Smooth flowing gradient animation */
        @keyframes gradientFlow {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        .stApp {
            background: linear-gradient(135deg, #ff758c, #ff7eb3, #76c7c0, #06beb6, #48b1bf);
            background-size: 400% 400%;
            animation: gradientFlow 20s infinite ease-in-out;
            color: black;
            position: relative;
            overflow: hidden;
            min-height: 100vh;
            perspective: 1000px; /* Adds depth */
        }

        /* Floating 3D bubbles */
        .bubble {
            position: absolute;
            width: 60px;
            height: 60px;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.6) 30%, rgba(255, 255, 255, 0.2) 100%);
            border-radius: 50%;
            animation: bubbleMove 15s infinite ease-in-out;
            box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.5);
            transform: translateZ(50px) scale(1.2);
        }

        @keyframes bubbleMove {
            0% {transform: translateY(100vh) translateZ(0px) scale(0.5);}
            50% {transform: translateY(-10vh) translateZ(50px) scale(1.2);}
            100% {transform: translateY(-100vh) translateZ(100px) scale(0.5);}
        }

        /* Generate multiple bubbles with 3D effect */
        .bubble:nth-child(1) { left: 5%; animation-duration: 10s; width: 70px; height: 70px; }
        .bubble:nth-child(2) { left: 15%; animation-duration: 12s; width: 50px; height: 50px; }
        .bubble:nth-child(3) { left: 25%; animation-duration: 14s; width: 80px; height: 80px; }
        .bubble:nth-child(4) { left: 35%; animation-duration: 16s; width: 60px; height: 60px; }
        .bubble:nth-child(5) { left: 45%; animation-duration: 18s; width: 90px; height: 90px; }
        .bubble:nth-child(6) { left: 55%; animation-duration: 20s; width: 75px; height: 75px; }
        .bubble:nth-child(7) { left: 65%; animation-duration: 22s; width: 85px; height: 85px; }
        .bubble:nth-child(8) { left: 75%; animation-duration: 24s; width: 95px; height: 95px; }
        .bubble:nth-child(9) { left: 85%; animation-duration: 26s; width: 100px; height: 100px; }
        .bubble:nth-child(10) { left: 95%; animation-duration: 28s; width: 110px; height: 110px; }
        
        /* Tag Bubble Styling */
        .tag-container { display: flex; flex-wrap: wrap; gap: 10px; }
        .tag {
            background: linear-gradient(135deg, #06beb6, #48b1bf);
            color: white; padding: 8px 14px; font-size: 16px;
            border-radius: 20px; font-weight: bold;
            box-shadow: 3px 3px 7px rgba(0,0,0,0.3);
            transition: transform 0.3s ease-in-out;
        }
        .tag:hover { transform: scale(1.1); }

    </style>

    <div class="bubble"></div>
    <div class="bubble"></div>
    <div class="bubble"></div>
    <div class="bubble"></div>
    <div class="bubble"></div>
    <div class="bubble"></div>
    <div class="bubble"></div>
    <div class="bubble"></div>
    <div class="bubble"></div>
    <div class="bubble"></div>
""", unsafe_allow_html=True)

st.title("🔥 Multi-Label Classification with 3D Floating Bubbles 🔥")

# **Input box for user text**
test_texts = st.text_area("✍ **Enter your article:**", height=200, value="20 Fastest Programming Languages in 2025 to Speed Up Development...")
test_texts = text_pre_processing(test_texts)

# **Predict button**
# if st.button("✨ Generate Tags"):
predicted_tags = predict_tags(test_texts)

# # Display predicted tags
# st.write("### 🏷️ Predicted Tags:")

# tag_html = '<div class="tag-container">'
# for tag in predicted_tags:
#     tag_html += f'<span class="tag">{tag}</span>'
# tag_html += '</div>'

# st.markdown(tag_html, unsafe_allow_html=True)



# **Predict button**
if st.button("✨ Generate Tags"):
    predicted_tags = predict_tags(test_texts)

    # Display predicted tags
    st.write("### 🏷️ Predicted Tags:")
    
    tag_html = '<div class="tag-container">'
    for tag in predicted_tags:
        tag_html += f'<span class="tag">{tag}</span>'
    tag_html += '</div>'
    
    st.markdown(tag_html, unsafe_allow_html=True)
