import requests
r = requests.get("https://data.cityofnewyork.us/api/views/9umc-3b2y/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/capital-grants/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/capital-grants/data.csv"]
