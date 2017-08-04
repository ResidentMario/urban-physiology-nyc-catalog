import requests
r = requests.get("https://data.cityofnewyork.us/api/views/68rr-d3jr/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/health-and-human-services-prequalification-catalog/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/health-and-human-services-prequalification-catalog/data.csv"]
