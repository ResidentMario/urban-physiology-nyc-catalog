import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ita7-8em7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tenure-of-officers-against-whom-allegations-were-substantiated-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tenure-of-officers-against-whom-allegations-were-substantiated-2005-2009/data.csv"]
