import requests
r = requests.get("https://data.cityofnewyork.us/api/views/a9yv-r6p4/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/communities-potentially-eligible-for-community-wastewater-management-program-funds/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/communities-potentially-eligible-for-community-wastewater-management-program-funds/data.csv"]
