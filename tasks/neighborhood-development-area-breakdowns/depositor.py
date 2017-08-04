import requests
r = requests.get("https://data.cityofnewyork.us/api/views/urvc-2kdr/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/neighborhood-development-area-breakdowns/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/neighborhood-development-area-breakdowns/data.csv"]
