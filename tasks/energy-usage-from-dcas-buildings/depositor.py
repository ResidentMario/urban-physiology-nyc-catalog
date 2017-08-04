import requests
r = requests.get("https://data.cityofnewyork.us/api/views/pwva-zn2w/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/energy-usage-from-dcas-buildings/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/energy-usage-from-dcas-buildings/data.csv"]
