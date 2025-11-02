import streamlit as st
import time
from puzzle_generator import generate_puzzle
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine

#fixing the UI for header and buttons
st.title("🧠 Bingo: Your Math Tutor") #, unsafe_allow_html = True)

st.markdown('''
    <style>
        /* General page background & alignment */
        .main {
            text-align: centre;
        }
        /* Title styling */
        h1 {
            color: black !important;
            font-weight: 800 !important;
            font-size: 3em !important;
        }
            
        /* Subtitle (Current Level etc.) */
        h3, h4 {
            color: black !important;
            font-weight: 600 !important;
            font-size: 1.5em !important;
        }
        /* Text input */
        -stTextInput > div > div > input {
            text-align: center;
            font-size: 1.2em;
            font-weight: 500;
        }
        /* Buttons */
        .stButtons > button {
            background-color: #333;
            color: black !important;
            font-size: 1em;
            border-radius: 8px;
            padding: 10px 24px;
            font-weight: bold;
        }
            .stButton > button:hover{
            background-color: #555;
            color: #f0f0f0;
        }
    </style>
''', unsafe_allow_html=True)

# adding background
page_bg = '''
<style>
[data-testid= "stAppViewContainer"] {
    background-image: url("https://i.pinimg.com/736x/16/85/ca/1685ca63601d68b5729b7b215a5021c7.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    color: white !important;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
[data-testid="stSidebar"] {
    background-color: rgba(255,255,255,0.8);
}
</style>
'''
st.markdown(page_bg, unsafe_allow_html=True)

if 'tracker' not in st.session_state:
    st.session_state.tracker = PerformanceTracker()
if 'engine' not in st.session_state:
    st.session_state.engine = AdaptiveEngine()
if 'difficulty' not in st.session_state:
    st.session_state.difficulty = st.selectbox("Choose starting level:", ['easy', 'medium', 'hard', 'extreme'])
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

st.subheader(f"Current Level: {st.session_state.difficulty.capitalize()}")
question, answer = generate_puzzle(st.session_state.difficulty)
st.write(f"**Solve:** {question}")

user_answer = st.text_input("Your answer:")
if st.button("Submit"):
    start = time.time() if st.session_state.start_time is None else st.session_state.start_time
    correct = str(user_answer).strip() == str(answer)
    response_time = round(time.time() - start, 2)
    st.session_state.tracker.log_attempt(question, correct, response_time, st.session_state.difficulty)
    stats = st.session_state.tracker.summary()

    if stats:
        next_diff = st.session_state.engine.predict_next_level(stats['accuracy'], stats['avg_time'])
        st.session_state.difficulty = next_diff
        st.success(f"✅ {'Correct!' if correct else '❌ Wrong.'} Next level: {next_diff.capitalize()}")
    st.session_state.start_time = time.time()

if st.button("Show Summary"):
    st.write(st.session_state.tracker.get_dataframe())
    st.write(st.session_state.tracker.summary())

