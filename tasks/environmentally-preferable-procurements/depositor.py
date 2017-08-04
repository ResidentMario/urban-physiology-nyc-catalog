import requests
r = requests.get("https://data.cityofnewyork.us/download/294z-97kb/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/environmentally-preferable-procurements/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/environmentally-preferable-procurements/data.xlsx"]
