import requests
r = requests.get("https://data.cityofnewyork.us/api/views/qg7h-jiy8/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fdny-vital-statistics/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fdny-vital-statistics/data.csv"]
