import requests
r = requests.get("https://data.cityofnewyork.us/api/views/rbrz-iagc/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/assignment-of-officers-against-whom-allegations-were-substantiated/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/assignment-of-officers-against-whom-allegations-were-substantiated/data.csv"]
