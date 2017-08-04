import requests
r = requests.get("https://data.cityofnewyork.us/download/kjk4-7tzy/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2040-population-projection-tables/data.xlsx", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2040-population-projection-tables/data.xlsx"]
