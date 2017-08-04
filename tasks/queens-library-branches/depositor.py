import requests
r = requests.get("https://data.cityofnewyork.us/api/views/kh3d-xhq7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/queens-library-branches/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/queens-library-branches/data.csv"]
