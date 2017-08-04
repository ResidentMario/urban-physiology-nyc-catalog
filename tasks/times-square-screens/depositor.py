import requests
r = requests.get("https://data.cityofnewyork.us/api/views/n246-cev5/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/times-square-screens/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/times-square-screens/data.csv"]
