# Cricket Data Scraper

## Overview

This project is a web scraper that extracts batting statistics from Cricbuzz for matches played between 2011 and 2020. The data includes player names, dismissal mode, runs scored, balls faced, fours, sixes, strike rate, innings, location, date, batting position, format, year, match name, and series name. The extracted data is saved into a CSV file named `Batting_Info.csv`.

## Project Plan

### **1. Data Source Identification**

- The scraper fetches match data from [Cricbuzz](https://www.cricbuzz.com) using archived scorecards.
- The base URL for each year is structured as: `https://www.cricbuzz.com/cricket-scorecard-archives/{year}`.

### **2. Extracting Series URLs**

- The script first fetches the list of series played in a given year.
- Each series page contains multiple matches, so it collects the URLs of all matches in that series.

### **3. Extracting Match Information**

- For each match, the scraper finds the scoreboard URL.
- The script extracts:
  - **Game format** (Test, ODI, or T20)
  - **Match name**
  - **Series name**
  - **Location**
  - **Date**
  - **Year**

### **4. Extracting Batting Data**

- The scraper parses batting scorecards for up to four innings per match.
- For each batsman, the following details are extracted:
  - **Name**
  - **Mode of dismissal**
  - **Runs scored**
  - **Balls faced**
  - **Fours**
  - **Sixes**
  - **Strike rate**
  - **Batting position**
  - **Innings number**

### **5. Saving Data**

- All extracted information is stored in a Pandas DataFrame.
- The DataFrame is then exported to a CSV file named `Batting_Info.csv`.

## Modifications and Enhancements

- **Modified in Google Studio**: The extracted data and analytics were further refined using Google AI Studio.
- **Data Feed into Google AI Studio**: The extracted cricket data was uploaded to Google AI Studio for model training and fine-tuning.
- **Finetuned API for Function Calls**: A custom AI model was fine-tuned using Google AI Studio and integrated with the project for predictive analytics.
- **Integration with Gemini API**: Implemented Gemini API to enhance data analysis and prediction.
- **Frontend using Streamlit**: Built an interactive frontend using Streamlit to visualize and explore the extracted cricket data in real-time.

## Installation & Usage

### **Prerequisites**

Ensure you have the following dependencies installed:

```bash
pip install requests pandas numpy beautifulsoup4 streamlit
```

### **Running the Script**

Execute the script using:

```bash
python script.py
```

This will start scraping Cricbuzz and generate `Batting_Info.csv` with all the required details.

### **Running the Streamlit App**

To launch the interactive dashboard, run:

```bash
streamlit run app.py
```

## Notes

- The scraper might be blocked due to repeated requests, so adding time delays or rotating proxies can improve stability.
- This project is for educational purposes only and should not be used for commercial scraping without Cricbuzz's permission.

## Future Improvements

- Implement multi-threading to speed up the scraping process.
- Add error handling for missing or inconsistent data.
- Support live match updates.
- Extract bowling and fielding statistics.
- Expand Streamlit app with additional filters and visualizations.

## Author

Developed by Mani Deep
