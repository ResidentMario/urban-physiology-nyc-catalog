import requests
r = requests.get("https://data.cityofnewyork.us/api/views/q2ni-ztsb/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-council-discretionary-funding/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-council-discretionary-funding/data.csv"]
