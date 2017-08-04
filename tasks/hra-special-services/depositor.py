import requests
r = requests.get("https://data.cityofnewyork.us/api/views/dfad-fpwf/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hra-special-services/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hra-special-services/data.csv"]
