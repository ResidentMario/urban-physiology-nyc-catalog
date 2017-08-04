import requests
r = requests.get("https://data.cityofnewyork.us/api/views/gepv-dxc2/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy16-mmr-spending-and-budget-information-by-units-of-appropriation/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy16-mmr-spending-and-budget-information-by-units-of-appropriation/data.csv"]
