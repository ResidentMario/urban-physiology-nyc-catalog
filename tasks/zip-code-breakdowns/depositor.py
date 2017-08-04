import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6bic-qvek/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/zip-code-breakdowns/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/zip-code-breakdowns/data.csv"]
