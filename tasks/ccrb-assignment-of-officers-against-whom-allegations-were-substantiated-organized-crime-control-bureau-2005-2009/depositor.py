import requests
r = requests.get("https://data.cityofnewyork.us/api/views/xt3u-h44z/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-organized-crime-control-bureau-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-organized-crime-control-bureau-2005-2009/data.csv"]
