import requests
r = requests.get("https://data.cityofnewyork.us/api/views/pzqy-pk76/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/residence-of-subject-officers-against-whom-allegations-were-substantiated-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/residence-of-subject-officers-against-whom-allegations-were-substantiated-2005-2009/data.csv"]
