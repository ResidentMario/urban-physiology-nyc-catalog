import requests
r = requests.get("https://data.cityofnewyork.us/api/views/nre2-6m2s/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/consumer-services-mediated-complaints/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/consumer-services-mediated-complaints/data.csv"]
