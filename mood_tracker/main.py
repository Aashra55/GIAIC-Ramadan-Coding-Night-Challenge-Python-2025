import streamlit as st # For creating the web app
import pandas as pd # For data manipulation
import datetime # For handling dates
import csv # For reading and writing CSV files
import os # For file operations

MOOD_FILE = "mood_log.csv"

# Function to load the mood data
def load_mood_data():
    # If path does not exist, return an empty DataFrame
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["date", "mood"])
    return pd.read_csv(MOOD_FILE)

# Function to save the mood data
def save_mood_data():
    