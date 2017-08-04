import requests
r = requests.get("https://data.cityofnewyork.us/api/views/uvw5-9znb/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/council-members/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/council-members/data.csv"]
