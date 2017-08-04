import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6bgk-3dad/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dob-ecb-violations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dob-ecb-violations/data.csv"]
