import requests
r = requests.get("https://data.cityofnewyork.us/api/views/a8wp-rerh/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/self-hauler-registrants/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/self-hauler-registrants/data.csv"]
