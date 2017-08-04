import requests
r = requests.get("https://data.cityofnewyork.us/api/views/vi6e-zw9u/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dob-license-fees/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dob-license-fees/data.csv"]
