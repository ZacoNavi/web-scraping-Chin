import requests
from bs4 import BeautifulSoup
url = 'https://reg.summit.snowflake.com/flow/snowflake/summit24/speakers/page/catalog?_ga=2.214326751.937231384.1716904967-1746399976.1716500779'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
items = soup.find_all('li')
for item in items:
    print(item.get_text())
