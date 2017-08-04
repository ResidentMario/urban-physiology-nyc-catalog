import requests
r = requests.get("https://data.cityofnewyork.us/api/views/2ij3-wj64/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-other-bureaus-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-other-bureaus-2005-2009/data.csv"]
