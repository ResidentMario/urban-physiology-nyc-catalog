import requests
r = requests.get("https://data.cityofnewyork.us/api/views/nthg-fsts/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-patrol-borough-brooklyn-south-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-assignment-of-officers-against-whom-allegations-were-substantiated-patrol-borough-brooklyn-south-2005-2009/data.csv"]
