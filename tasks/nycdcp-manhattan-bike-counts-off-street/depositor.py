import requests
r = requests.get("https://data.cityofnewyork.us/api/views/mfmf-gtvc/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycdcp-manhattan-bike-counts-off-street/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycdcp-manhattan-bike-counts-off-street/data.csv"]
