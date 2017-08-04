import requests
r = requests.get("https://data.cityofnewyork.us/api/views/4vf7-wwbk/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/capital-commitments-city-funds/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/capital-commitments-city-funds/data.csv"]
