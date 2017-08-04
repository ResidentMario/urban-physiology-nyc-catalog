import requests
r = requests.get("https://data.cityofnewyork.us/api/views/k548-32d3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inmate-incidents-inmate-fights/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inmate-incidents-inmate-fights/data.csv"]
