import requests
r = requests.get("https://data.cityofnewyork.us/api/views/dvaj-b7yx/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/shelter-repair-scorecard/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/shelter-repair-scorecard/data.csv"]
