import requests
r = requests.get("https://data.cityofnewyork.us/api/views/tesz-9suw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/capacity-project-site-location/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/capacity-project-site-location/data.csv"]
