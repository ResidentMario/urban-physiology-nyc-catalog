import requests
r = requests.get("https://data.cityofnewyork.us/api/views/59kj-x8nc/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/housing-litigations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/housing-litigations/data.csv"]
