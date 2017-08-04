import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ibs4-k445/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medicaid-offices/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medicaid-offices/data.csv"]
