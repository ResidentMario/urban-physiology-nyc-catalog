import requests
r = requests.get("https://data.cityofnewyork.us/api/views/tbf6-u8ea/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hra-domestic-violence-partners/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hra-domestic-violence-partners/data.csv"]
