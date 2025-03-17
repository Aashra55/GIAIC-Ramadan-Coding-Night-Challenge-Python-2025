# Quiz App

## Overview
This is a simple quiz application built using Streamlit. It presents random multiple-choice questions to the user and keeps track of their score. The quiz refreshes after each answer submission.

## Features
- Randomized questions from a predefined list.
- Multiple-choice answer selection.
- Instant feedback on correct/incorrect answers.
- Score tracking across multiple questions.
- Aesthetic UI with colored score display.
- Auto-refresh after answering to show a new question.

## Installation
To run this application, make sure you have Python and UV installed. Then install Streamlit:
```bash
pip install streamlit
```
Or with Virtual Environment (Optional):
```bash
uv add streamlit
```

## Activate Virtual Environment (If Created)
For Windows:
```bash
.venv\Scripts\activate
```
For macOS/Linux:
```bash
source venv/bin/activate
```

## Running the App
Execute the following command in your terminal:
```bash
streamlit run app.py
```
Replace `app.py` with the filename of the script.

## Customization
- You can add more questions to the `quiz_questions` list.
- Modify the UI styles using `st.markdown`.
- Enhance interactivity by adding timers or animations.
- Customize the score display and add sound effects for correct/wrong answers.

## Future Improvements
- Add different difficulty levels.
- Include a final score summary at the end of the quiz.
- Implement a leaderboard to track high scores.
- Add more categories and allow users to select their preferred quiz topics.

