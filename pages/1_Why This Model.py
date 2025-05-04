import streamlit as st

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
        <div class="problem-title">🎯 Why This Model?</div>
        <div class="problem-text">
            This machine learning model is designed to <b>predict relevant tags</b> for Medium articles based on their textual content. 
            Since a single article can span multiple topics, this is a <span class="highlight">multi-label classification</span> task where the model assigns <b>multiple tags</b> to each article. <br><br>
            <ul>
                <li><span class="highlight">✅ Better Content Organization:</span> Helps group articles by topic for easier navigation.</li>
                <li><span class="highlight">✅ Improved Discoverability:</span> Enhances search and recommendation systems by tagging content accurately.</li>
                <li><span class="highlight">✅ Writer Assistance:</span> Automatically suggests appropriate tags to authors, saving time.</li>
                <li><span class="highlight">✅ Scalable Tagging Automation:</span> Useful for platforms managing large volumes of content.</li>
            </ul>
            Just input your article’s text, and the model will return the most suitable tags! 🔮
        </div>
    </div>
""", unsafe_allow_html=True)



# Keep your animated gradient background and bubbles
st.markdown("""
    <style>
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
            perspective: 1000px;
        }

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


# Predict button with animation and gradient styling
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
        bubble-button:visited {
            color: white !important;  /* Ensures clicked link stays white */
        }   
    </style>

    <div class="bubble-button-container">
        <a href="/Predict" class="bubble-button">🔍 Try Tag Prediction</a>
    </div>
""", unsafe_allow_html=True)
