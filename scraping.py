import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

def series(url):
    series_url = []
    response = requests.get(url).content
    soup3 = BeautifulSoup(response, 'html.parser')
    all_series = soup3.find('div', class_='cb-col-84 cb-col').findAll('div', class_='cb-srs-lst-itm')
    for series in all_series:
        series_url.append("https://www.cricbuzz.com" + series.a['href'])
    return series_url

def matches_url(series_url):
    match_urls = []
    response = requests.get(series_url).content
    soup2 = BeautifulSoup(response, 'html.parser')
    matches = soup2.findAll('div', class_='cb-col-60 cb-col cb-srs-mtchs-tm')
    for match in matches:
        match_urls.append("https://www.cricbuzz.com" + match.a['href'])
    return match_urls

def find_format(url):
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'html.parser')
    content = soup.find('span', itemprop='description')['content'].lower()
    if 'test' in content:
        return 'Test'
    elif 'odi' in content:
        return 'ODI'
    elif 't20' in content:
        return 'T20'
    return ''

def find_match(url):
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'html.parser')
    return soup.find('div', class_='cb-billing-plans-text cb-team-lft-item').h1.text

def find_series(url):
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'html.parser')
    return soup.find('div', class_='cb-nav-subhdr cb-font-12').a['title']

def scoreboard(url):
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'html.parser')
    tags = soup.findAll('a', class_='cb-nav-tab')
    for tag in tags:
        if tag.text == 'Scorecard':
            return "https://www.cricbuzz.com" + tag['href']
    return ''
print("Started!")
batsman_info = []
for i in range(2020, 2021):
    series_urls = series(f'https://www.cricbuzz.com/cricket-scorecard-archives/{i}')
    for series_url in series_urls:
        match_urls = matches_url(series_url)
        for url in match_urls:
            scoreboard_url = scoreboard(url)
            if not scoreboard_url:
                continue
            game_format = find_format(scoreboard_url)
            match_name = find_match(scoreboard_url)
            series_name = find_series(scoreboard_url)
            
            scoreboard_response = requests.get(scoreboard_url).content
            soup1 = BeautifulSoup(scoreboard_response, 'html.parser')
            location = soup1.find('a', itemprop='location').text.strip()
            date = soup1.find('span', itemprop='startDate').text.strip()
            year = soup1.find('div', class_='cb-nav-subhdr cb-font-12').a.text.split()[-1]

            for i in range(1, 5):
                innings = soup1.find('div', id=f"innings_{i}")
                if innings:
                    scrd_items = innings.find('div', class_='cb-col cb-col-100 cb-ltst-wgt-hdr').findAll('div', class_='cb-col cb-col-100 cb-scrd-itms')
                    if scrd_items[-1].find('div', class_='cb-col cb-col-27') is None:
                        scrd_items = scrd_items[:-2]
                    else:
                        scrd_items = scrd_items[:-3]
                    
                    for pos, scrd_item in enumerate(scrd_items):
                        name = scrd_item.find('a', class_='cb-text-link').text.strip()
                        runs = scrd_item.find('div', class_='cb-col cb-col-8 text-right text-bold').text
                        dismissal_mode = scrd_item.find('div', class_='cb-col cb-col-33').text.strip()
                        scrd_tags = scrd_item.findAll('div', class_='cb-col cb-col-8 text-right')

                        balls = scrd_tags[0].text.strip() if len(scrd_tags) > 0 else ''
                        fours = scrd_tags[1].text.strip() if len(scrd_tags) > 1 else ''
                        sixes = scrd_tags[2].text.strip() if len(scrd_tags) > 2 else ''
                        strike_rates = scrd_tags[3].text.strip() if len(scrd_tags) > 3 else ''

                        batsman_info.append([name, dismissal_mode, runs, balls, fours, sixes, strike_rates, i, location, date, pos + 1, game_format, year, match_name, series_name])

df = pd.DataFrame(batsman_info, columns=['Batsman', 'Mode of Dismissal', 'Runs Scored', 'Balls Faced', 'Fours', 'Sixes', 'Strike Rate', 'Innings', 'Location', 'Date', 'Batting Position', 'Format', 'Year', 'Match', 'Series'])
df.to_csv('Batting_Info.csv', index=False)
