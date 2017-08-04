import requests
r = requests.get("https://data.cityofnewyork.us/api/views/7cqi-bt79/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/special-event-concession-fee-details/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/special-event-concession-fee-details/data.csv"]
