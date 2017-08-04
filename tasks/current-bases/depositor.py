import requests
r = requests.get("https://data.cityofnewyork.us/api/views/eccv-9dzr/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/current-bases/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/current-bases/data.csv"]
