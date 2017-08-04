import requests
r = requests.get("https://data.cityofnewyork.us/api/views/nsu8-kyp7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ceps-organization-information/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ceps-organization-information/data.csv"]
