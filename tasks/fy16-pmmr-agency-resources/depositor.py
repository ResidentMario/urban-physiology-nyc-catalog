import requests
r = requests.get("https://data.cityofnewyork.us/api/views/7ceq-6nwu/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy16-pmmr-agency-resources/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy16-pmmr-agency-resources/data.csv"]
