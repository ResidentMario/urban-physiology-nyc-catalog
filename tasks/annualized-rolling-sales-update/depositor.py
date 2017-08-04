import requests
r = requests.get("https://data.cityofnewyork.us/download/uzf5-f8n2/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/annualized-rolling-sales-update/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/annualized-rolling-sales-update/data.zip"]
