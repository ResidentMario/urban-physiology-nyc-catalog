import requests
r = requests.get("https://data.cityofnewyork.us/api/views/5c4s-jwtq/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/total-snap-recipients/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/total-snap-recipients/data.csv"]
