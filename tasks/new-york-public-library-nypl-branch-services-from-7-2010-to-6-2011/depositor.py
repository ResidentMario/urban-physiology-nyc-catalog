import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ne9z-skhf/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-public-library-nypl-branch-services-from-7-2010-to-6-2011/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-public-library-nypl-branch-services-from-7-2010-to-6-2011/data.csv"]
