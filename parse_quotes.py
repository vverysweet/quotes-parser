import requests
from bs4 import BeautifulSoup
import pandas as pd


response = requests.get("https://quotes.toscrape.com")
html = response.text
soup = BeautifulSoup(html, "html.parser")

data = {"Цитата": [], "Автор": []}

text = soup.find_all(class_="text")
authors = soup.find_all(class_="author")
for t, a in zip(text, authors):
    data["Цитата"].append(t.text)
    data["Автор"].append(a.text)
df = pd.DataFrame(data)
df.to_excel("quotes.xlsx", index=False)