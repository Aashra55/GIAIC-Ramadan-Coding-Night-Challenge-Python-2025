import streamlit as st # For creating the web app
import pandas as pd # For data manipulation
import datetime # For handling dates
import csv # For reading and writing CSV files
import os # For file operations

MOOD_FILE = "mood_log.csv"

# Function to load the mood data
def load_mood_data():
    
    if not os.path.exists(MOOD_FILE): # If path does not exist, return an empty DataFrame
        return pd.DataFrame(columns=["Date", "Mood"]) # Creates an empty DataFrame with columns "date" and "mood"
    
    return pd.read_csv(MOOD_FILE) # Reads the CSV file and returns a DataFrame


# Function to save the mood data
def save_mood_data(date, selected_mood):
    
    with open (MOOD_FILE, mode='a', newline='') as file:
        
        writer = csv.writer(file) # Creates a CSV writer object that allows us to write data to the CSV file in a structured way
        writer.writerow([date, selected_mood]) # Writes the date and mood to the CSV file
        

today = datetime.date.today() # Gets the current date
    
# Streamlit UI

st.set_page_config(
    page_title="Mood Tracker",
    page_icon=":smiley:",
)
st.title("🎭 Mood Insights 📊") # Sets the title of the web app

st.subheader("How are you feeling today?😃") # Adds a subheader to the web app

mood_options = {
    "😊 Happy": "Happy",
    "😐 Neutral": "Neutral",
    "😢 Sad": "Sad",
    "😡 Angry": "Angry"
}

mood = st.selectbox("Select your mood", list(mood_options.keys())) # Creates a dropdown menu for selecting the mood
selected_mood = mood_options[mood] # Get the text value

if st.button("💾 Log My Mood"): # Creates a button that, when clicked, executes the code block below
    
    save_mood_data(today, selected_mood) # Saves the mood data to the CSV file
    st.success("💖 Mood Logged! Hope you have a great day! 🌞") # Displays a success message
    
data = load_mood_data() # Loads the mood data

if not data.empty: # Checks if the DataFrame is not empty
    
    st.subheader("📈 Mood Trends Over Time") # Adds a subheader to the web app
    
    data["Date"] = pd.to_datetime(data["Date"]) # Converts the "Date" column to a datetime format while preserving all other columns
    
    mood_counts = data.groupby("Mood").count()["Date"] # Groups the data by "mood" and counts the number of occurrences of each mood
    
    st.bar_chart(mood_counts)
     
    st.subheader("🔍 Recent Mood Check-Ins") # Adds a subheader to the web app
    
    st.dataframe(data.tail()) # Displays the last 5 rows of the DataFrame
    
    # Download Button for Mood History
    st.download_button(
        label="📥 Download Mood History",
        data=data.to_csv(index=False),
        file_name="mood_logs.csv",
        mime="text/csv"
    )

else: # If the DataFrame is empty, display a message
    
    st.info("No mood data available. Log your mood to see trends over time.") # Displays an informational message
    

