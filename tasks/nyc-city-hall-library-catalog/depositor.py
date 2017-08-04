import requests
r = requests.get("https://data.cityofnewyork.us/api/views/gysc-yn4h/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-city-hall-library-catalog/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-city-hall-library-catalog/data.csv"]
