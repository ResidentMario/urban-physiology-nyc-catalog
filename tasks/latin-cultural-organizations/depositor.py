import requests
r = requests.get("https://data.cityofnewyork.us/api/views/799n-b76v/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/latin-cultural-organizations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/latin-cultural-organizations/data.csv"]
