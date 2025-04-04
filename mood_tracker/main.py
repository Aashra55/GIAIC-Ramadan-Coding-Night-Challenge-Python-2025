import streamlit as st # For creating the web app
import pandas as pd # For data manipulation
import datetime # For handling dates
import csv # For reading and writing CSV files
import os # For file operations

MOOD_FILE = "mood_data.csv"

# Function
def delete_mood_file():
    if os.path.exists(MOOD_FILE):
        os.remove(MOOD_FILE)
        
# Function to ensure the mood file exists
def ensure_mood_file():
    if not os.path.exists(MOOD_FILE):  
        with open(MOOD_FILE, mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Mood"])  # Ensure headers exist

ensure_mood_file()  

# Function to load the mood data
def load_mood_data():
    
    if not os.path.exists(MOOD_FILE): # If path does not exist, return an empty DataFrame
        return pd.DataFrame(columns=["Date", "Mood"]) # Creates an empty DataFrame with columns "date" and "mood"
    
    try :
        data = pd.read_csv(MOOD_FILE,encoding="utf-8") # Reads the CSV file and stores the data in a DataFrame
        if "Date" not in data.columns or "Mood" not in data.columns:
            return pd.DataFrame(columns=["Date", "Mood"]) # Creates an empty DataFrame with columns "date" and "mood"
        return data # Returns the DataFrame
    except Exception as e:
        st.error(f"Error loading mood data: {e}")
        return pd.DataFrame(columns=["Date", "Mood"])

# Function to save the mood data
def save_mood_data(date, mood):
    
    with open (MOOD_FILE, mode='a', newline='', encoding="utf-8") as file:
        
        writer = csv.writer(file) # Creates a CSV writer object that allows us to write data to the CSV file in a structured way
        writer.writerow([date, mood]) # Writes the date and mood to the CSV file
        

today = datetime.date.today() # Gets the current date
    
# Streamlit UI

st.set_page_config(
    page_title="Mood Tracker",
    page_icon=":smiley:",
)
st.title("🎭 Mood Insights 📊") # Sets the title of the web app

st.subheader("How are you feeling today?😃") # Adds a subheader to the web app

mood_options = [
    "😊 Happy",
    "😐 Neutral",
    "😢 Sad",
    "😡 Angry"
]

mood = st.selectbox("Select your mood", mood_options) # Creates a dropdown menu for selecting the mood

if "mood_data" not in st.session_state:
    st.session_state.mood_data = load_mood_data()

if "first_run" not in st.session_state:
    delete_mood_file()
    st.session_state.first_run = True

if st.button("💾 Log My Mood"): # Creates a button that, when clicked, executes the code block below
    
    save_mood_data(today, mood) # Saves the mood data to the CSV file
    st.success("💖 Mood Logged! Hope you have a great day! 🌞") # Displays a success message
    
data = load_mood_data() # Loads the mood data

if not data.empty and "Date" in data.columns and "Mood" in data.columns: # Checks if the DataFrame is not empty
    
    st.subheader("📈 Mood Trends Over Time") # Adds a subheader to the web app
    
    try: 
        data["Date"] = pd.to_datetime(data["Date"], errors="coerce") # Converts the "Date" column to a datetime format while preserving all other columns
        data = data.dropna(subset=["Date"]) # Drops rows with missing dates
    
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
        
    except Exception as e:
        st.error(f"Error processing mood data: {e}")
        
else: # If the DataFrame is empty, display a message
    
    st.info("No mood data available. Log your mood to see trends over time.") # Displays an informational message
    

