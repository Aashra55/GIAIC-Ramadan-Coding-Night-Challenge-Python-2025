# Time Zone Converter App

This is a **Streamlit-based Time Zone Converter App** that allows users to:
- View the current time in multiple time zones.
- Convert time between different time zones.

## Features
- Displays the **current time** for selected time zones.
- Allows users to **select a time** and convert it from one time zone to another.
- Uses the `datetime` module for time manipulation.
- Uses `ZoneInfo` to handle different time zones efficiently.

## Technologies Used
- **Python**
- **UV (Universal Vectorization)** (Used for managing dependencies and environment) 
- **Streamlit** (for the web app UI)
- **datetime** (for date and time handling)
- **zoneinfo** (for time zone conversion)

## Installation
- **Pre-requisites**
Install Python and UV

1. **Initialize the Project**
   ```sh
   uv init time-zone-app
   cd time-zone-app
   ```

2. **Install Streamlit**
```sh
uv add streamlit
```

3. **Activate Virtual Environment**
   ```sh
   source venv/bin/activate  # On macOS/Linux
   .venv\Scripts\activate  # On Windows
   ```

4. **Run the Application**
   ```sh
   streamlit run app.py
   ```

## Usage
1. **Select multiple time zones** from the multi-select dropdown to view current time.
2. **Select a specific time** from the time input field.
3. Choose the **'From TimeZone'** and **'To TimeZone'**.
4. Click **'Convert Time'** to get the converted time.

## File Structure
```
📂 time-zone-app
│── app.py  # Main application file
│── README.md  # Project documentation
```

## Dependencies
- `streamlit`
- `datetime`
- `ZoneInfo`

## License
This project is **open-source** under the MIT License.

---

**Enjoy using the Time Zone Converter App!** 🚀

