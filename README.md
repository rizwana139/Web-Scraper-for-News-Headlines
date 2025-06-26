# Web-Scraper-for-News-Headlines

This project is a Python-based web scraper that automatically collects top news headlines from a news website using `requests` and `BeautifulSoup`.



**Objective**

To scrape top headlines from [The Hindu News](https://www.thehindu.com/news/) and save them into a `.txt` file.


**Tools & Technologies**

- Python

- `requests` – for sending HTTP requests

- `BeautifulSoup` – for parsing HTML content

---

**Files**

- `web_scraper.py` – Python script for scraping headlines

- `headlines.txt` – Output file containing scraped headlines

**How It Works**

1. Sends a GET request to the website.

2. Parses the HTML content using BeautifulSoup.

3. Extracts all headlines (`<h3>` tags).

4. Prints headlines and saves them into `headlines.txt` with numbering.
 
**Outcome:** Automate data collection from a public website

Rizwana Vempalli 

**Email ID:** rrizzu139@gmail.com 