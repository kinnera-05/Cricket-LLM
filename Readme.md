# Cricket Data Scraper  

## Overview  

This project is a web scraper that extracts batting statistics from Cricbuzz for matches played between 2011 and 2020. The extracted data includes player names, dismissal mode, runs scored, balls faced, fours, sixes, strike rate, innings, location, date, batting position, format, year, match name, and series name. The extracted data is saved into a CSV file named `Batting_Info.csv`.  

## Workflow  

1. **Data Extraction**  
   - The scraper collects match scorecards from Cricbuzz archives.  
   - It first fetches all series played in a given year.  
   - Then, it extracts match URLs from each series and retrieves the detailed scorecards.  
   - The script parses batting scorecards, extracting statistics for each player.  

2. **Data Processing**  
   - The extracted data is structured into a Pandas DataFrame.  
   - The data is cleaned and formatted to ensure consistency.  
   - The processed data is saved into `Batting_Info.csv`.  

3. **Integration with Google AI Studio**  
   - The CSV file is uploaded to Google AI Studio.  
   - A custom AI model is trained using this dataset to analyze batting performance trends.  
   - The model is fine-tuned to enhance predictive capabilities.  

4. **Creating the Gemini API**  
   - The fine-tuned model from Google AI Studio is deployed as an API using Gemini AI.  
   - The API enables advanced analytics, including player performance predictions and insights.  

5. **Frontend Development using Streamlit**  
   - A Streamlit dashboard is built for real-time interaction.  
   - Users can explore statistics, based on their query.  

## Installation & Usage  

### **Prerequisites**  
Ensure you have the required dependencies installed:  

```bash
pip install requests pandas numpy beautifulsoup4 streamlit
```  

### **Running the Scraper**  
Run the script to extract and save batting data:  

```bash
python script.py
```  

### **Launching the Streamlit Dashboard**  
To visualize the data interactively:  

```bash
streamlit run app.py
```  

## Future Enhancements  

- **Optimized Scraping**: Implement multi-threading for faster data collection.  
- **Live Match Updates**: Extend functionality to fetch live match data.  
- **Comprehensive Analytics**: Include bowling and fielding statistics.  
- **Enhanced Visualization**: Add more filters and interactive elements in the Streamlit app.  

## Author  

Developed by Kinnera and Team.
