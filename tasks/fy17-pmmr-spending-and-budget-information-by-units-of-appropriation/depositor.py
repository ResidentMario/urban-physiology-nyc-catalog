import requests
r = requests.get("https://data.cityofnewyork.us/api/views/jjvq-4t2v/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy17-pmmr-spending-and-budget-information-by-units-of-appropriation/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy17-pmmr-spending-and-budget-information-by-units-of-appropriation/data.csv"]
