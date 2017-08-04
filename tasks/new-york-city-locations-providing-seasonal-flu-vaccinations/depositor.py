import requests
r = requests.get("https://data.cityofnewyork.us/api/views/w9ei-idxz/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-locations-providing-seasonal-flu-vaccinations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-locations-providing-seasonal-flu-vaccinations/data.csv"]
