import requests
r = requests.get("https://data.cityofnewyork.us/api/views/4vsa-fhnm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/reasons-for-police-civilian-encounters-that-led-to-a-complaint-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/reasons-for-police-civilian-encounters-that-led-to-a-complaint-2005-2009/data.csv"]
