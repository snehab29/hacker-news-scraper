# Grab the page
import requests
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser') #magnifying glass that organizes the html page

problems = soup.find_all("span", class_="text")

authors = soup.find_all("small", class_="author")

for problem, author_item in zip(problems, authors):
    title = problem.get_text().strip()
    link = author_item.get_text().strip()
    print(f"{title}: {link}")
