import requests
r = requests.get("https://data.cityofnewyork.us/api/views/bty7-2jhb/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/historical-dob-permit-issuance/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/historical-dob-permit-issuance/data.csv"]
