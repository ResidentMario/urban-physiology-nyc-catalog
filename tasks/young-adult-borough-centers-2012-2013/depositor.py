import requests
r = requests.get("https://data.cityofnewyork.us/api/views/pfn4-vjwr/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/young-adult-borough-centers-2012-2013/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/young-adult-borough-centers-2012-2013/data.csv"]
