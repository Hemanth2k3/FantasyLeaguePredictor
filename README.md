# Fantasy League Predictor

Predict winning Fantasy Cricket teams using web scraping, data analysis, and model construction.

## Project Overview

This project aims to assist Fantasy Cricket enthusiasts in creating winning teams for contests on platforms like Dream11. By leveraging web scraping, data analysis, and model construction, the project generates optimal teams based on player statistics, maximizing the chances of success in contests.

## Key Skills
- Python
- Web Scraping
- Algorithms
- Django

## Key Features

- **Algorithm for Team Generation:**
  - Generate all combinations (22C11) of players from both teams with specific conditions.
  - Apply filters to analyze and shortlist teams based on player statistics and performance.

- **Web Scraping Player Stats:**
  - Scrape player statistics, especially batting averages, from ESPN Cricinfo website.
  - Store the scraped data in a dictionary for easy access during team analysis.

- **Optimal Team Selection:**
  - Sum up player stats for each of the 500,000+ generated teams.
  - Sort teams in descending order based on the aggregated stats.
  - Select top teams as potential winning combinations.

## Algorithm Explanation

### Step 1: Team Generation
- Generate all combinations of 11 players from both teams with specific conditions (e.g., a wicketkeeper in each team, a batsman).
- Resulting in over 500,000 teams.

### Step 2: Web Scraping Player Stats
- Scrape player statistics, particularly batting averages, from ESPN Cricinfo.
- Store the stats in a dictionary for easy access and analysis.

### Step 3: Team Analysis and Selection
- Sum up player stats for each of the 500,000+ teams.
- Sort teams in descending order based on aggregated stats.
- Select top teams as potential winning combinations.

## Project Purpose

- **Strategic Advantage:** This tool provides Fantasy Cricket enthusiasts with a strategic advantage in creating winning teams. It leverages web scraping, data analysis, and model construction to optimize team selection based on player statistics.
- **Financial Potential:** With a modest entry fee of 50 rupees, users can secure 500 chances for a total of 25,000 rupees in a 1 Cr Contest. Winning with any of these teams has the potential to yield returns surpassing the initial investment.

## Tech Stack

- Python
- Web Scraping
- Django
