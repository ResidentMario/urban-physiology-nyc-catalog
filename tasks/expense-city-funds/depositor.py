import requests
r = requests.get("https://data.cityofnewyork.us/api/views/kzk6-y58k/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/expense-city-funds/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/expense-city-funds/data.csv"]
