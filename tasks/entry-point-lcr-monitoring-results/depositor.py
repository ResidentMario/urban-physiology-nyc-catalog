import requests
r = requests.get("https://data.cityofnewyork.us/api/views/aa5e-digs/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/entry-point-lcr-monitoring-results/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/entry-point-lcr-monitoring-results/data.csv"]
