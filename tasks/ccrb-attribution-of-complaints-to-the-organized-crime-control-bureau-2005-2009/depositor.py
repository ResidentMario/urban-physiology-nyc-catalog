import requests
r = requests.get("https://data.cityofnewyork.us/api/views/v3a6-muuw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-attribution-of-complaints-to-the-organized-crime-control-bureau-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-attribution-of-complaints-to-the-organized-crime-control-bureau-2005-2009/data.csv"]
