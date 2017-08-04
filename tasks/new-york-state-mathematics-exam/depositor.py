import requests
r = requests.get("https://data.cityofnewyork.us/api/views/r75y-8qe7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-state-mathematics-exam/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-state-mathematics-exam/data.csv"]
