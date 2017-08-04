import requests
r = requests.get("https://data.cityofnewyork.us/api/views/tzwr-vksx/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-capacity-program-by-borough/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-capacity-program-by-borough/data.csv"]
