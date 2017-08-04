import requests
r = requests.get("https://data.cityofnewyork.us/api/views/d4uz-6jaw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inmate-arrests/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inmate-arrests/data.csv"]
