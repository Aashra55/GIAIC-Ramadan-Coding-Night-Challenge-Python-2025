import streamlit as st # for UI of the web app
from datetime import datetime  # Imports the datetime module for handling date and time operations
from zoneinfo import ZoneInfo  # Imports the ZoneInfo module to work with time zones
import time # For adding a delay effect

# list of available timezones
TIME_ZONES = [
  "UTC",
  "Europe/London",
  "America/New_York",
  "America/Chicago",
  "America/Denver",
  "America/Los_Angeles",
  "Asia/Karachi",
  "Asia/Kolkata",
  "Asia/Dubai",
  "Asia/Tokyo",
  "Asia/Shanghai",
  "Asia/Singapore",
  "Australia/Sydney",
  "Africa/Cairo",
  "Africa/Lagos",
  "Europe/Berlin",
  "Europe/Paris",
  "Europe/Moscow",
  "Pacific/Auckland",
  "Pacific/Honolulu"
]

#Streamlit UI
st.set_page_config(
    page_title="TimeZone App",
    page_icon="⏰"
)

st.title("⏰ Time Zone App")

# Create a multiselect widget for selecting TimeZones
selected_timezone = st.multiselect("Select TimeZones", TIME_ZONES, default=["UTC","Asia/Karachi"])

st.subheader("🕒 Selected TimeZones")

# Display the selected TimeZones
if selected_timezone:
    for timezone in selected_timezone: # loop to display TimeZones
        # Get the current time of selected TimeZones
        current_time = datetime.now(ZoneInfo(timezone)).strftime("%Y-%m-%d %H:%M:%S")
        st.write(f"**{timezone}**: {current_time}")

# Converting time between different TimeZones
st.subheader("🔄 Convert Time Between TimeZones")

# Create input field to select the time which is to be converted
selected_time = st.time_input("⏳ Select Time")

# Create a selectbox for selecting the timezone to convert from
from_timezone = st.selectbox("From TimeZone", TIME_ZONES, index=0)

# Create a selectbox for selecting the timezone to convert to
to_timezone = st.selectbox("To_TimeZone", TIME_ZONES, index=6)

# Convert the time between the selected TimeZones
if st.button("🚀 Convert Time"):
    with st.spinner("Converting time..."):
        time.sleep(2)  # Add a small delay for animation
        date_time = datetime.combine(datetime.today(), selected_time, tzinfo=ZoneInfo(from_timezone))
        converted_time = date_time.astimezone(ZoneInfo(to_timezone)).strftime("%Y-%m-%d %H:%M:%S")
    
    st.success(f"✅ Converted Time from **{from_timezone}** to **{to_timezone}**: **{converted_time}**")
    
    

