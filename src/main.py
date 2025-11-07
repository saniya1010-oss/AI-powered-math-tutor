# Author: Saniya | For evaluation purposes only | © 2025

import streamlit as st
import time
from puzzle_generator import generate_puzzle
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine

# --- Basic UI ---
st.title("🧠 Bingo: Your Math Tutor 🧠")

st.markdown('''
    <style>
        h1 {
            color: white !important;
            font-weight: 800 !important;
            font-size: 2.8em !important;
            text-align: center;
        }
        h3, h4, p, label {
            color: white !important;
            font-weight: 600 !important;
            text-align: center;
        }
        .stTextInput > div > div > input {
            text-align: center;
            font-size: 1.1em;
            font-weight: 500;
        }
        .stButton > button {
            background-color: black;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 8px 18px;
        }
        .stButton > button:hover {
            background-color: #444;
            color: #fff;
        }
    </style>
''', unsafe_allow_html=True)

if 'name' not in st.session_state:
    st.session_state.name = ""
if 'tracker' not in st.session_state:
    st.session_state.tracker = PerformanceTracker()
if 'engine' not in st.session_state:
    st.session_state.engine = AdaptiveEngine()
if 'difficulty' not in st.session_state:
    st.session_state.difficulty = 'easy'
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'question' not in st.session_state or 'answer' not in st.session_state:
    st.session_state.question, st.session_state.answer = generate_puzzle(st.session_state.difficulty)

# --- NAME INPUT and QUIZ ---
st.session_state.name = st.text_input("Enter your name:", st.session_state.name)

st.markdown(f"<h4>Current Level: {st.session_state.difficulty.capitalize()}</h4>", unsafe_allow_html=True)
st.markdown(f"<h4 style='color:black;'>Solve: {st.session_state.question}</h4>", unsafe_allow_html=True)

user_answer = st.text_input("Your answer:")

if st.button("Submit"):
    if not st.session_state.name.strip():
        st.warning("Please enter your name before starting.")
    else:
        start = st.session_state.start_time or time.time()
        response_time = round(time.time() - start, 2)
        correct = str(user_answer).strip() == str(st.session_state.answer)

        st.session_state.tracker.log_attempt(
            st.session_state.question, correct, response_time, st.session_state.difficulty
        )

        stats = st.session_state.tracker.summary()
        if stats:
            next_diff = st.session_state.engine.predict_next_level(stats['accuracy'], stats['avg_time'])
            st.session_state.difficulty = next_diff
            st.success(f"{'✅ Correct! Please press show summary to move to the next question' if correct else '❌ Oops!! Try again.. Please press show summary to move forward'} Next level: {next_diff.capitalize()}")

        # Generate new question
        st.session_state.question, st.session_state.answer = generate_puzzle(st.session_state.difficulty)
        st.session_state.start_time = time.time()

if st.button("Show Summary"):
    st.write(f"**Name:** {st.session_state.name}")
    st.write(st.session_state.tracker.get_dataframe())
    st.write(st.session_state.tracker.summary())

