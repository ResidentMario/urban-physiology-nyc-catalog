import requests
r = requests.get("https://data.cityofnewyork.us/api/views/aagv-t6fa/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy17-pmmr-agency-resources/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy17-pmmr-agency-resources/data.csv"]
