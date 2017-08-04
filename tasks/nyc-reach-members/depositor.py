import requests
r = requests.get("https://data.cityofnewyork.us/api/views/7btz-mnc8/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-reach-members/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-reach-members/data.csv"]
