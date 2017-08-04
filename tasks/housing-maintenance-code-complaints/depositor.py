import requests
r = requests.get("https://data.cityofnewyork.us/api/views/uwyv-629c/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/housing-maintenance-code-complaints/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/housing-maintenance-code-complaints/data.csv"]
