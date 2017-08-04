import requests
r = requests.get("https://data.cityofnewyork.us/api/views/q5za-zqz7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy16-pmmr-agency-performance-indicators/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy16-pmmr-agency-performance-indicators/data.csv"]
