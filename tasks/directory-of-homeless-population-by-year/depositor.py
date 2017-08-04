import requests
r = requests.get("https://data.cityofnewyork.us/api/views/5t4n-d72c/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-homeless-population-by-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-homeless-population-by-year/data.csv"]
