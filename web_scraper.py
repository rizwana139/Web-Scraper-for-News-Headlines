import requests
from bs4 import BeautifulSoup

URL = 'https://www.thehindu.com/news/'
response = requests.get(URL)
print("The response code is :", response)

# Parse HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the news headlines from HTML
headlines = soup.find_all('h3')

# Open a file to write the headlines
with open("G:/My Drive/Colab Notebooks/headlines.txt", "w", encoding="utf-8") as file:
    # Display and write the headlines
    for i, headline in enumerate(headlines, 1):
        clean_text = headline.text.strip()
        print(f"{i}. {clean_text}\n")
        file.write(f"{i}. {clean_text}\n\n") 