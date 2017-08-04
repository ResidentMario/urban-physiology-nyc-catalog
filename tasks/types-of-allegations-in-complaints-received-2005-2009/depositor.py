import requests
r = requests.get("https://data.cityofnewyork.us/api/views/jp7y-czvr/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/types-of-allegations-in-complaints-received-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/types-of-allegations-in-complaints-received-2005-2009/data.csv"]
