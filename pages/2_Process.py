import streamlit as st

# Page Configuration
st.set_page_config(page_title="AI-Powered Medium Tag Prediction", page_icon="📖", layout="wide")

# Apply Custom CSS for Animated Background & Floating Bubbles
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
        min-height: 100vh;
        padding: 20px;
    }

    /* Floating bubbles */
    .bubble {
        position: absolute;
        width: 80px;
        height: 80px;
        background: radial-gradient(circle, rgba(255, 255, 255, 0.6) 30%, rgba(255, 255, 255, 0.2) 100%);
        border-radius: 50%;
        animation: bubbleMove 10s infinite ease-in-out;
        box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.5);
    }

    @keyframes bubbleMove {
        0% {transform: translateY(100vh) scale(0.5);}
        50% {transform: translateY(-10vh) scale(1.2);}
        100% {transform: translateY(-100vh) scale(0.5);}
    }

    /* Text Box for Improved Readability */
    .text-container {
        background: rgba(255, 255, 255, 0.5);
        padding: 20px;
        border-radius: 10px;
        width: 85%;
        margin: auto;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.3);
    }

    /* Section Formatting */
    .section-title { font-size:28px; font-weight:bold; color:#2E3A46; text-align:center; }
    .highlight { font-size:20px; font-weight:bold; color:#27AE60; }
    .sub-text { font-size:16px; color:#2E3A46; text-align:justify; }
    .separator { border-top: 2px solid #BDC3C7; margin-top: 10px; margin-bottom: 10px; }

    </style>

    <div class="bubble"></div>
    <div class="bubble"></div>
    <div class="bubble"></div>
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


# Title & Introduction inside Text Box
st.write(f"""
    <div class="text-container">
        <h1 class="section-title">🔍Building a Multi-Label Classification Model for Medium Tag Prediction with Streamlit</h1>
        <h3>Introduction</h3>
         <p class="sub-text">
            Predicting relevant tags for Medium articles using <b>machine learning</b> requires a well-structured pipeline. This blog provides a comprehensive step-by-step guide, covering everything from <b>data collection</b> to <b>deployment</b> using <b>Streamlit</b>, ensuring a smooth and engaging <b>UI/UX</b> experience.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('<hr class="separator">', unsafe_allow_html=True)

# **📊 Data Collection**
st.markdown("""
    <div class="text-container">
        <h2 class="section-title">📊 Data Collection</h2>
        <p class="sub-text">Since Medium does not provide an API for direct access, Selenium and BeautifulSoup were used to scrape articles and their tags.</p>
        <div>
            <h3 class="highlight">✅ Web Scraping Methods</h3>
            <ul>
                <li><b>Selenium:</b> Automated browser interactions to load dynamic content.</li>
                <li><b>BeautifulSoup:</b> Parsed HTML elements to extract article titles and tags.</li>
            </ul>
        </div>
        <div>
            <h3 class="highlight">🔹 Challenges & Solutions</h3>
            <ul>
                <li>💡 <b>Dynamic Class Names:</b> Medium assigns different CSS classes upon each page refresh.</li>
                <li>✅ <i>Solution:</i> Used <code>find_next_sibling()</code> in BeautifulSoup to dynamically locate elements.</li>
                <li>💡 <b>Lazy Loading & Infinite Scrolling:</b> Medium loads articles dynamically as users scroll.</li>
                <li>✅ <i>Solution:</i> Implemented Selenium’s <code>execute_script()</code> to automate scrolling and capture additional articles.</li>
            </ul>
        </div>
        <div>
            <h3 class="highlight">📂 Data Storage & Cleaning</h3>
            <ul>
                <li>Extracted data was stored in a structured CSV format.</li>
                <li>Duplicate articles were removed using <code>drop_duplicates()</code>.</li>
                <li>Missing values were handled using <code>dropna()</code> to maintain clean data.</li>
            </ul>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<hr class="separator">', unsafe_allow_html=True)

# 🛠️ **Data Preprocessing**
st.markdown("""
    <div class="text-container">
        <h2 class="section-title">🛠️ Data Preprocessing</h2>
        <p class="sub-text">Before training, raw text must be cleaned and transformed to enhance model efficiency.</p>
    <div>
        <h3 class="highlight">✅ Applied Preprocessing Techniques</h3>
        <ul>
            <li>✔ <b>Stop Word Removal:</b> Eliminated common words that add little meaning.</li>
            <li>✔ <b>Accent Handling:</b> Normalized accented characters using <code>unicodedata.normalize()</code>.</li>
            <li>✔ <b>Fixing Contractions:</b> Converted "you're" → "you are" for standardization.</li>
            <li>✔ <b>Emoji Removal:</b> Used the <code>emoji</code> module to filter unnecessary symbols.</li>
            <li>✔ <b>Stemming & Lowercasing:</b> Reduced words to root form for uniform representation.</li>
        </ul>
    </div>
    <div>
        <h3 class="highlight">📊 Feature Engineering: TF-IDF Vectorization</h3>
        <p class="sub-text">
            TF-IDF (Term Frequency-Inverse Document Frequency) was applied to convert text into numerical features.
            This technique captures important words while minimizing the impact of frequently occurring terms.
        </p>
    <div>
        <h3 class="highlight">🎯 Target Label Encoding</h3>
        <p class="sub-text">
            Since Medium articles can have multiple associated tags, <b>MultiLabelBinarizer</b> converted categorical labels into a binary matrix format,
            making them suitable for multi-label classification.
        </p>
    </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<hr class="separator">', unsafe_allow_html=True)

# 🛠️ **Data Preprocessing**
st.markdown("""
    <div class="text-container">
        <h2 class="section-title">🛠️ Data Preprocessing</h2>
        <p class="sub-text">Before training, raw text must be cleaned and transformed to enhance model efficiency.</p>
    <div>
        <h3 class="highlight">✅ Applied Preprocessing Techniques</h3>
        <ul>
            <li>✔ <b>Stop Word Removal:</b> Eliminated common words that add little meaning.</li>
            <li>✔ <b>Accent Handling:</b> Normalized accented characters using <code>unicodedata.normalize()</code>.</li>
            <li>✔ <b>Fixing Contractions:</b> Converted "you're" → "you are" for standardization.</li>
            <li>✔ <b>Emoji Removal:</b> Used the <code>emoji</code> module to filter unnecessary symbols.</li>
            <li>✔ <b>Stemming & Lowercasing:</b> Reduced words to root form for uniform representation.</li>
        </ul>
    </div>
    <div>
        <h3 class="highlight">📊 Feature Engineering: TF-IDF Vectorization</h3>
        <p class="sub-text">
            TF-IDF (Term Frequency-Inverse Document Frequency) was applied to convert text into numerical features.
            This technique captures important words while minimizing the impact of frequently occurring terms.
        </p>
    </div>
    <div>
        <h3 class="highlight">🎯 Target Label Encoding</h3>
        <p class="sub-text">
            Since Medium articles can have multiple associated tags, <b>MultiLabelBinarizer</b> converted categorical labels into a binary matrix format,
            making them suitable for multi-label classification.
        </p>
    </div>
    </div>
""", unsafe_allow_html=True)


st.markdown('<hr class="separator">', unsafe_allow_html=True)

# 🚀 **Training the Model**
st.markdown("""
    <div class="text-container">
        <h2 class="section-title">🚀 Training the Model</h2>
        <p class="sub-text">To train the model effectively, we used TF-IDF transformed data and handled multi-label classification appropriately.</p>
        <div>
        <h3 class="highlight">✅ Training Pipeline</h3>
        <ul>
            <li>✔ <b>Used Complete Dataset:</b> Ensured TF-IDF transformed data was utilized for robust learning.</li>
            <li>✔ <b>Implemented MultiLabelBinarizer:</b> Properly handled multiple tags per article for multi-label classification.</li>
            <li>✔ <b>Optimized Learning Process:</b> Tuned hyperparameters using Optuna for better model efficiency.</li>
        </ul>
        </div>
        <div>
        <h3 class="highlight">📈 Performance Evaluation During Training</h3>
        <ul>
            <li>✅ <b>Hamming Loss:</b> Measures label misclassification. Lower values indicate better accuracy.</li>
            <li>✅ <b>Jaccard Score (Macro-Averaged):</b> Assesses intersection-over-union between predicted and actual tags, ensuring balanced evaluation across all labels.</li>
        </ul>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<hr class="separator">', unsafe_allow_html=True)


# 📈 **Evaluation Metrics**
st.markdown("""
    <div class="text-container">
        <h2 class="section-title">📈 Evaluation Metrics</h2>
        <p class="sub-text">Since multi-label classification requires specialized metrics beyond traditional accuracy, the following were applied:</p>
        <div>
        <h3 class="highlight">✅ Applied Evaluation Metrics</h3>
        <ul>
            <li>✔ <b>Hamming Loss:</b> Fraction of incorrectly predicted labels per instance.</li>
            <li>✔ <b>Jaccard Score (Macro-Averaged):</b> Ensures fair evaluation across frequent and rare labels.</li>
        </ul>
        </div>
        <div>
        <h3 class="highlight">🔹 Why These Metrics?</h3>
        <ul>
            <li>🔹 <b>Hamming Loss:</b> Captures misclassification rates per tag, ensuring no labels are overlooked.</li>
            <li>🔹 <b>Jaccard Score:</b> Assesses prediction accuracy, particularly for imbalanced datasets.</li>
        </ul>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<hr class="separator">', unsafe_allow_html=True)

# 🌐 **Deployment Using Streamlit**
st.markdown("""
    <div class="text-container">
        <h2 class="section-title">🌐 Deployment Using Streamlit</h2>
        <p class="sub-text">
            Once the model was successfully trained and evaluated, it was deployed via Streamlit, providing an interactive and user-friendly experience.
        </p>
        <div>
        <h3 class="highlight">✅ Why Streamlit?</h3>
        <ul>
            <li>💡 <b>Simple & Fast:</b> No need for additional backend development.</li>
            <li>💡 <b>Interactive Web Interface:</b> Users can input an article and receive predicted tags instantly.</li>
            <li>💡 <b>Python-Based Deployment:</b> Easily integrates machine learning workflows.</li>
        </ul>
        </div>
        <div>
        <h3 class="highlight">📌 Streamlit Webpage Features</h3>
        <ul>
            <li>✅ <b>Text Input Box:</b> Users enter article content.</li>
            <li>✅ <b>Real-Time Predictions:</b> ML model returns relevant Medium tags.</li>
            <li>✅ <b>Stylish UI/UX Design:</b> Clean, modern interface with improved readability.</li>
        </ul>
        </div>
        <div>
        <h3 class="highlight">🚀 Hosting the Web Application</h3>
        <p class="sub-text">
            The webpage was successfully hosted using Streamlit, making it accessible globally.
        </p>
        </div>
    </div>
""", unsafe_allow_html=True)
