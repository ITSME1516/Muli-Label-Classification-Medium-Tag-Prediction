import streamlit as st

# Problem Statement Page
st.markdown("""
        
    <style>
            .stApp { background-color: #FFFFFF !important; }
        .problem-container {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 20px;
            width: 80%;
            margin: auto;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        }

        .problem-title {
            font-size: 30px;
            font-weight: bold;
            text-align: center;
            color: #FF4181;
        }

        .problem-text {
            font-size: 18px;
            text-align: left;
            line-height: 1.6;
            color: #333;
        }

        .highlight {
            color: red;
            font-weight: bold;
        }
    </style>

    <div class="problem-container">
        <div class="problem-title">🔥 Problem Statement 🔥</div>
        <div class="problem-text">
            Medium is a popular blogging platform where writers publish content on various topics. Each article is assigned tags that help categorize content and improve discoverability. <br><br>
            However, many writers struggle to choose the right tags, leading to:
            <ul>
                <li class="highlight">⚠ Poor content categorization.</li>
                <li class="highlight">⚠ Reduced visibility in search and recommendations.</li>
                <li class="highlight">⚠ Mismatched articles under irrelevant topics.</li>
            </ul>
            This project aims to automate tag prediction for Medium articles using machine learning. Given an article’s title and content, our model will predict the most relevant tags. 🚀
        </div>
    </div>
""", unsafe_allow_html=True)
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



# Button to navigate to predict.py
st.title("🌸 AI-Powered Tag Predictor 🌸",)
a,b,c = st.columns([4,2,4])

# b.page_link("pages/3_Predict.py", label="🔍 Try Tag Prediction", icon="🔮")
import streamlit as st

# Inject CSS styling for a button-like page link
st.markdown("""
    <style>
        .bubble-button-container {
            text-align: center;
            margin-top: 30px;
        }

        .bubble-button {
            padding: 12px 24px;
            font-size: 20px;
            font-weight: bold;
            border-radius: 50px;
            color: white;
            background: linear-gradient(135deg, #06beb6, #48b1bf);
            box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
            display: inline-block;
            cursor: pointer;
            text-decoration: none;
        }

        .bubble-button:hover {
            transform: scale(1.1);
            box-shadow: 0px 6px 15px rgba(0,0,0,0.4);
        }

    </style>

    <div class="bubble-button-container">
        <a href="/Predict" class="bubble-button">🔍 Try Tag Prediction</a>
    </div>
""", unsafe_allow_html=True)
import os

st.write(os.listdir("pages/"))
