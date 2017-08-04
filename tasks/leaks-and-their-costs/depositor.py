import requests
r = requests.get("https://data.cityofnewyork.us/api/views/3nm4-g97k/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/leaks-and-their-costs/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/leaks-and-their-costs/data.csv"]
