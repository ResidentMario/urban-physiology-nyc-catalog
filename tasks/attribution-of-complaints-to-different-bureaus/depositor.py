import requests
r = requests.get("https://data.cityofnewyork.us/api/views/wwsa-q2dq/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/attribution-of-complaints-to-different-bureaus/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/attribution-of-complaints-to-different-bureaus/data.csv"]
