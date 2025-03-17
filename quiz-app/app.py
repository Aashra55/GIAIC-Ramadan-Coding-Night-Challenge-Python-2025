import streamlit as st
import random 
import time

# Configure Streamlit page settings
st.set_page_config(page_title="Quiz App", page_icon="📑")

# Title of the app
st.title("📑 Quiz App")

# List of quiz questions with options and correct answers
quiz_questions = [
    {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    {"question": "Which programming language is known as the 'mother of all languages'?", "options": ["Python", "C", "Java", "Assembly"], "answer": "C"},
    {"question": "What is the hardest natural substance on Earth?", "options": ["Gold", "Iron", "Diamond", "Platinum"], "answer": "Diamond"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Jupiter", "Mars", "Saturn"], "answer": "Mars"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["Mark Twain", "Harper Lee", "J.K. Rowling", "Ernest Hemingway"], "answer": "Harper Lee"},
    {"question": "What is the smallest unit of life?", "options": ["Atom", "Molecule", "Cell", "Organ"], "answer": "Cell"},
    {"question": "What does HTTP stand for?", "options": ["HyperText Transfer Protocol", "High-Tech Transfer Protocol", "HyperText Transmission Process", "Hyperlink Text Processing"], "answer": "HyperText Transfer Protocol"},
    {"question": "Which animal is known as the 'King of the Jungle'?", "options": ["Elephant", "Tiger", "Lion", "Cheetah"], "answer": "Lion"},
    {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Gd", "Go"], "answer": "Au"},
    {"question": "Which continent is the largest by land area?", "options": ["Africa", "North America", "Asia", "Europe"], "answer": "Asia"}
]

# Initialize session state for tracking current question
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(quiz_questions)

# Initialize session state for tracking score
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

# Get the current question
question = st.session_state.current_question

# Display question and score in two columns
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader(question["question"])  # Show the question
    
with col2:
    # Display score with custom styling
    st.markdown(
        f'<h3 style="color:  #E4599C;">Score: <b>{st.session_state.quiz_score}</b></h3>',
        unsafe_allow_html=True
    )

# Display multiple-choice options as radio buttons
selected_option = st.radio("Select an option", question["options"], key="answer")

# Submit answer button
if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.session_state.quiz_score += 1  # Increase score if correct
        st.success("Correct! 🎉 You got **1** point!")
    else:
        st.error("Incorrect! 😢 You got **0**")
        st.info(f"The correct answer is: **{question['answer']}**")
    
    time.sleep(3)  # Wait for 3 seconds before showing the next question
    
    # Select a new random question
    st.session_state.current_question = random.choice(quiz_questions)
    
    st.rerun()  # Refresh the app to display the new question
