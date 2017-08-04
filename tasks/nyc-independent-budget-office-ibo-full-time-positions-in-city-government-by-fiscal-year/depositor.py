import requests
r = requests.get("https://data.cityofnewyork.us/api/views/uaj7-9szf/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-independent-budget-office-ibo-full-time-positions-in-city-government-by-fiscal-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-independent-budget-office-ibo-full-time-positions-in-city-government-by-fiscal-year/data.csv"]
