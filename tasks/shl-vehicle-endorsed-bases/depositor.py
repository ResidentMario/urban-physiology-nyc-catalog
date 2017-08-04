import requests
r = requests.get("https://data.cityofnewyork.us/api/views/rvyk-uci3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/shl-vehicle-endorsed-bases/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/shl-vehicle-endorsed-bases/data.csv"]
