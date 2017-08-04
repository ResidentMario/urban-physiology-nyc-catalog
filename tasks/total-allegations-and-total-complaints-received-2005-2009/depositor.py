import requests
r = requests.get("https://data.cityofnewyork.us/api/views/bbvw-ivc8/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/total-allegations-and-total-complaints-received-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/total-allegations-and-total-complaints-received-2005-2009/data.csv"]
