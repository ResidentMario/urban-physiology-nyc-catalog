import requests
r = requests.get("https://data.cityofnewyork.us/api/views/x8rc-3utf/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/race-of-victims-whose-allegations-were-substantiated-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/race-of-victims-whose-allegations-were-substantiated-2005-2009/data.csv"]
