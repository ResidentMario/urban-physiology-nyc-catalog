import requests
r = requests.get("https://data.cityofnewyork.us/api/views/mqdy-gu73/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/city-store-the-official-store-of-the-city-of-new-york/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/city-store-the-official-store-of-the-city-of-new-york/data.csv"]
