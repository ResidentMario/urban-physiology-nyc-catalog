import requests
r = requests.get("https://data.cityofnewyork.us/api/views/m6nh-ye6v/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/intake-within-and-outside-ccrb-jurisdiction/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/intake-within-and-outside-ccrb-jurisdiction/data.csv"]
