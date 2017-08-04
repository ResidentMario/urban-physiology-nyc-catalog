import requests
r = requests.get("https://data.cityofnewyork.us/api/views/c87b-2j3i/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-rearrest-rate-monthly-average/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-rearrest-rate-monthly-average/data.csv"]
