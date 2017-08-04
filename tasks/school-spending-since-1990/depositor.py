import requests
r = requests.get("https://data.cityofnewyork.us/api/views/p26e-k6k9/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-spending-since-1990/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-spending-since-1990/data.csv"]
