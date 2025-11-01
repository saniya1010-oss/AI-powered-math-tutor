import streamlit as st
import random, time
from adaptive_engine import predict_next, update_model

st.title("Math Adventures: Adaptive Learning Prototype")

if "difficulty" not in st.session_state:
    st.session_state.difficulty = 1
if "score" not in st.session_state:
    st.session_state.score = []
if "start" not in st.session_state:
    st.session_state.start = None

def generate_problem(level):
    a, b = random.randint(1, 10 * level), random.randint(1, 10 * level)
    op = random.choice(["+", "-", "*"])
    expr = f"{a} {op} {b}"
    return expr, eval(expr)

problem, answer = generate_problem(st.session_state.difficulty)
st.write(f"**Difficulty:** {st.session_state.difficulty}")
st.write(problem)

user_answer = st.number_input("Your answer:", step=1, format="%d")
if st.button("Submit"):
    start = st.session_state.start or time.time()
    correct = int(user_answer == answer)
    response_time = time.time() - start
    features = [st.session_state.difficulty, response_time, correct]

    target = 1 if correct and response_time < 5 else 0
    update_model(features, target)
    next_diff = st.session_state.difficulty + (1 if predict_next(features) else -1)
    st.session_state.difficulty = max(1, min(3, next_diff))

    st.session_state.score.append(correct)
    st.success("Correct!" if correct else "Try again!")
    st.session_state.start = time.time()
