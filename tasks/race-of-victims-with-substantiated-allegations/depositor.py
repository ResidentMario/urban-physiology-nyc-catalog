import requests
r = requests.get("https://data.cityofnewyork.us/api/views/mvhn-ypfv/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/race-of-victims-with-substantiated-allegations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/race-of-victims-with-substantiated-allegations/data.csv"]
