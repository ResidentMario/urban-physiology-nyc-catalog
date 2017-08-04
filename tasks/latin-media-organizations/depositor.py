import requests
r = requests.get("https://data.cityofnewyork.us/api/views/9z9b-6hvk/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/latin-media-organizations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/latin-media-organizations/data.csv"]
