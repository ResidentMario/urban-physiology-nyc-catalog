import requests
r = requests.get("https://data.cityofnewyork.us/api/views/yczb-msz7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fc-bid-walkof-fame-data/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fc-bid-walkof-fame-data/data.csv"]
