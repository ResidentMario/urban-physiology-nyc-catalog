import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6qzy-b4x8/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/total-housing-units-by-occupancy-status-and-tenure-by-borough/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/total-housing-units-by-occupancy-status-and-tenure-by-borough/data.csv"]
