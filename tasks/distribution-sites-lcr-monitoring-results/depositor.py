import requests
r = requests.get("https://data.cityofnewyork.us/api/views/g63j-swsd/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/distribution-sites-lcr-monitoring-results/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/distribution-sites-lcr-monitoring-results/data.csv"]
