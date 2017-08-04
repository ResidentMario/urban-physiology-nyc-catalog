import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hpid-63r5/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-municipal-building-energy-benchmarking-results-2014/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-municipal-building-energy-benchmarking-results-2014/data.csv"]
