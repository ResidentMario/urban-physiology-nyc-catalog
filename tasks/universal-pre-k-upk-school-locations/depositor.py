import requests
r = requests.get("https://data.cityofnewyork.us/api/views/kiyv-ks3f/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/universal-pre-k-upk-school-locations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/universal-pre-k-upk-school-locations/data.csv"]
