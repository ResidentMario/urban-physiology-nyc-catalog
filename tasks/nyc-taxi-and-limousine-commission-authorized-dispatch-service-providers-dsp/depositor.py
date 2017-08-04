import requests
r = requests.get("https://data.cityofnewyork.us/api/views/2n4x-d97d/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-taxi-and-limousine-commission-authorized-dispatch-service-providers-dsp/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-taxi-and-limousine-commission-authorized-dispatch-service-providers-dsp/data.csv"]
