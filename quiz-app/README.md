# Quiz App

A simple interactive quiz application built with [Streamlit](https://streamlit.io/). The app displays multiple-choice questions, tracks the user's score, and includes a countdown timer for each question. It also auto-refreshes the page every second to update the timer and implement a delay after each answer submission.

## Features

- **Multiple-Choice Questions:**  
  Presents questions with a set of answer options.
  
- **Score Tracking:**  
  Updates and displays the user's score in real-time.

- **Countdown Timer:**  
  Each question has a 10-second timer. If the time runs out, the app automatically loads a new question.

- **2-Second Delay After Submission:**  
  After submitting an answer, the app waits for 2 seconds (to display feedback) before moving to the next question.

- **Auto-Refresh:**  
  The app uses an auto-refresh mechanism to update the timer and check for the delay without blocking the UI.

- **Randomized Questions:**  
  A new random question is selected after each answer submission or when time expires.

## Prerequisites

- Python 3.7 or higher
- [Streamlit](https://streamlit.io/)
- [streamlit-autorefresh](https://github.com/randyzwitch/streamlit-autorefresh)

## Installation

1. **Clone the repository (if using version control):**

   ```bash
   git clone https://github.com/yourusername/quiz-app.git
   cd quiz-app
   ```

2. **Install the required packages:**

   ```bash
   pip install streamlit streamlit-autorefresh
   ```

## Running the App

To run the Quiz App, use the following command in your terminal:

```bash
streamlit run <your_script_name>.py
```

Replace `<your_script_name>.py` with the filename of your Streamlit quiz app script (e.g., `quiz_app.py`).

## Code Overview

- **Page Configuration and Title:**  
  The app sets the page title and icon using Streamlit’s configuration functions and displays the main title.

- **Quiz Questions Data:**  
  A list of dictionaries is defined to store quiz questions, options, and the correct answer.

- **Session State Initialization:**  
  Session state variables are used to store and persist the current question, score, timer, and submission status across app reruns.

- **Auto-Refresh Setup:**  
  The `st_autorefresh` function refreshes the app every second, ensuring that the countdown timer and submission delay work as expected.

- **User Interaction:**  
  The app displays multiple-choice options as radio buttons. Upon submitting an answer, the app checks the answer, updates the score, and provides immediate feedback.

- **Delay and Timer Logic:**  
  A non-blocking 2-second delay is implemented after an answer is submitted before a new question is loaded. A 10-second timer is also used to automatically advance the quiz if the user doesn't answer in time.

## Customization

You can customize the quiz by:
- **Modifying Questions:**  
  Update the `quiz_questions` list with your own questions, options, and answers.

- **Adjusting Timers:**  
  Change the values of the 10-second timer or the 2-second feedback delay as per your requirements.

- **Styling:**  
  Use custom CSS or HTML within Streamlit components to further style the UI.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/).
- Special thanks to the contributors of [streamlit-autorefresh](https://github.com/randyzwitch/streamlit-autorefresh).

