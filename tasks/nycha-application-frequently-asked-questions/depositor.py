import requests
r = requests.get("https://data.cityofnewyork.us/api/views/nkn9-ge6x/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycha-application-frequently-asked-questions/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycha-application-frequently-asked-questions/data.csv"]
