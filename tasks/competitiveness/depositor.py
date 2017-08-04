import requests
r = requests.get("https://data.cityofnewyork.us/download/5rx8-ct65/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/competitiveness/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/competitiveness/data.xlsx"]
