# Mood Tracker App

This is a simple **Mood Tracker** web application built using **Streamlit** and **Python**. It allows users to log their moods daily, visualize mood trends over time, and download their mood history. The app automatically resets data on refresh.

## Features
- **Log Your Mood**: Select your mood from a dropdown list and save it.
- **View Mood Trends**: See a bar chart of your mood trends over time.
- **Recent Mood Check-Ins**: View your most recent mood entries.
- **Download Mood History**: Download logged mood data as a CSV file.
- **Automatic Data Reset**: The logged data is deleted on every refresh/reload to start fresh.

## Technologies Used
- **Python**
- **Streamlit**
- **Pandas** (for data manipulation)
- **CSV Handling** (for saving and retrieving mood logs)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mood-tracker-app.git
   ```
2. Navigate to the project folder:
   ```bash
   cd mood-tracker-app
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## How It Works
1. **Logging Moods**: Users select their mood and log it.
2. **Data Storage**: Moods are temporarily saved in a CSV file (`mood_log.csv`).
3. **Automatic Data Reset**:
   - On refresh, the **CSV file is deleted** to reset data.
   - `st.cache_data.clear()` ensures cached data is removed.

## File Structure
```
📂 mood-tracker-app
│── app.py          # Main Streamlit application file
│── requirements.txt # Dependencies
│── README.md       # Documentation
```

## Deployment
To deploy the app on **Streamlit Cloud**:
1. Push the repository to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Connect your GitHub repo and deploy.

## License
This project is licensed under the MIT License.

