import requests
r = requests.get("https://data.cityofnewyork.us/api/views/w8dz-xpjh/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/referral-centers-for-high-school-alternatives/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/referral-centers-for-high-school-alternatives/data.csv"]
