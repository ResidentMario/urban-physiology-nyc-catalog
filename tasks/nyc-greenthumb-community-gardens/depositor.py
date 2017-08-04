import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ajxm-kzmj/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-greenthumb-community-gardens/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-greenthumb-community-gardens/data.csv"]
