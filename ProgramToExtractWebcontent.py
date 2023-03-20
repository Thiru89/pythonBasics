import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine_(2022%E2%80%93present)'

# Send GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract specific elements of the webpage
title = soup.title.text
body = soup.body.text

# Save the webpage content to a file
with open('output.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))
