import requests
r = requests.get("https://data.cityofnewyork.us/api/views/msp3-x6rs/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fdny-fire-department-fire-code-data/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fdny-fire-department-fire-code-data/data.csv"]
