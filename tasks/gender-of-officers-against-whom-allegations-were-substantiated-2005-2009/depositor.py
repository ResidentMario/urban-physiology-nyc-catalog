import requests
r = requests.get("https://data.cityofnewyork.us/api/views/664m-n5th/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/gender-of-officers-against-whom-allegations-were-substantiated-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/gender-of-officers-against-whom-allegations-were-substantiated-2005-2009/data.csv"]
