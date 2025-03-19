import streamlit as st # Import for building interactive web apps
import random # Import to randomly select quiz questions from a list.
import time # Import to work with time-related functions, like measuring elapsed time.

# Import the st_autorefresh function from the streamlit_autorefresh module,
# which allows the app to automatically refresh at set intervals.
from streamlit_autorefresh import st_autorefresh

# -------------------------------
# Page Configuration and Title
# -------------------------------
# Set the Streamlit page title and icon.
st.set_page_config(page_title="Quiz App", page_icon="📑")

# Display the main title of the app.
st.title("📑 Quiz App")

# -------------------------------
# Quiz Questions Data
# -------------------------------
# Define a list of dictionaries, each containing a question, a list of options, and the correct answer.
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

# -------------------------------
# Session State Initialization
# -------------------------------
# Session state helps in preserving the state between reruns.

# Current Question: Select a random question if not already set.
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(quiz_questions)
    
# Quiz Score: Initialize the score if not already set.
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
    
# Timer Start: Record the start time for the question timer.
if "timer_start" not in st.session_state:
    st.session_state.timer_start = time.time()
    
# Submitted Flag: To check whether the user has submitted an answer.
if "submitted" not in st.session_state:
    st.session_state.submitted = False
    
# Submission Time: To record the exact time when the answer was submitted.
if "submission_time" not in st.session_state:
    st.session_state.submission_time = None

# -------------------------------
# Auto-Refresh Setup
# -------------------------------
# Refresh the app every 1000 milliseconds (1 second) to update the timer and check for submission delay.
st_autorefresh(interval=1000, key="quiz_autorefresh")

# -------------------------------
# Displaying the Question and Score
# -------------------------------
# Retrieve the current question from session state.
question = st.session_state.current_question

# Display question and score in two columns
col1, col2 = st.columns([3, 1])
with col1:
    st.subheader(question["question"])
with col2:
    st.markdown(
        f'<h3 style="color:rgb(213, 63, 136);">Score: <b>{st.session_state.quiz_score}</b></h3>',
        unsafe_allow_html=True
    )
# -------------------------------
# User Interaction: Options and Submission
# -------------------------------
# Create two columns: one for answer options and one for the timer.
col1, col2 = st.columns(2)

with col1:
    # Display multiple-choice options as radio buttons
    selected_option = st.radio("Select an option", question["options"], key="answer")

# Submit answer button (only if not already submitted)
if st.button("Submit Answer") and not st.session_state.submitted:
    if selected_option == question["answer"]:
        st.session_state.quiz_score += 1  # Increase score if correct
    else:
        st.session_state.quiz_score += 0
        
    # Mark the question as submitted and record the submission time.
    st.session_state.submitted = True
    st.session_state.submission_time = time.time()  # Record submission time

# -------------------------------
# Handling the 2-Second Delay After Submission
# -------------------------------
# Check if an answer has been submitted.
if st.session_state.submitted:
    
    # Calculate how much time has passed since the submission.
    elapsed_since_submission = time.time() - st.session_state.submission_time
    
    if elapsed_since_submission >= 2:
        # After 2 seconds, load a new question and reset submission state
        st.session_state.current_question = random.choice(quiz_questions) # Select a new random question.
        st.session_state.timer_start = time.time()  # Reset the timer for the new question.
        st.session_state.submitted = False     # Reset the submitted flag.
        st.session_state.submission_time = None    # Clear the submission time.
        st.rerun()  # Rerun the app to update the UI with the new question.
    else:
        # While waiting for the 2-second delay to complete, show feedback based on the answer.
        if selected_option == question["answer"]:
            st.success("Correct! 🎉 You got **1** point!")
        else:
            st.error("Incorrect! 😢 You got **0**")
            st.info(f"The correct answer is: **{question['answer']}**")
# -------------------------------
# Timer Logic for Unanswered Questions
# -------------------------------
# If the answer is not submitted, display a countdown timer.
with col2:
    # Timer logic (active if answer is not submitted)
    if not st.session_state.submitted:
        total_time = 10  # Total allowed time (in seconds) for each question
        elapsed_time = int(time.time() - st.session_state.timer_start)
        remaining_time = total_time - elapsed_time

        if remaining_time > 0:
            # Show the remaining time to the user.
            st.info(f"⏳ Hurry up! Only **{remaining_time:02}** second(s) remaining! ⏰")
        else:
            # If the time is up, warn the user and load a new question.
            st.warning("⏳ Time's up! Moving to the next question...")
            st.session_state.current_question = random.choice(quiz_questions) # Select a new random question.
            st.session_state.timer_start = time.time()  # Reset timer
            st.rerun() # Rerun the app to update the UI.

