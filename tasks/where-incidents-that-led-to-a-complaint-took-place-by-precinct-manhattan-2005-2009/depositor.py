import requests
r = requests.get("https://data.cityofnewyork.us/api/views/fics-ewaq/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/where-incidents-that-led-to-a-complaint-took-place-by-precinct-manhattan-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/where-incidents-that-led-to-a-complaint-took-place-by-precinct-manhattan-2005-2009/data.csv"]
