import requests
r = requests.get("https://data.cityofnewyork.us/api/views/35cc-g4mc/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dep-cpr-data-from-july-2001-through-june-2011/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dep-cpr-data-from-july-2001-through-june-2011/data.csv"]
