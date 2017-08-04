import requests
r = requests.get("https://data.cityofnewyork.us/api/views/m3fi-rt3k/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-council-discretionary-funding-2009-2013/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-council-discretionary-funding-2009-2013/data.csv"]
