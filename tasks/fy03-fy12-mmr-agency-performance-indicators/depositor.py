import requests
r = requests.get("https://data.cityofnewyork.us/api/views/jhjm-vsp8/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy03-fy12-mmr-agency-performance-indicators/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fy03-fy12-mmr-agency-performance-indicators/data.csv"]
