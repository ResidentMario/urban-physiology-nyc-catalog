import requests
r = requests.get("https://data.cityofnewyork.us/api/views/q9kp-jvxv/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/acris-ucc-collateral-codes/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/acris-ucc-collateral-codes/data.csv"]
