import requests
r = requests.get("https://data.cityofnewyork.us/api/views/muaz-gc29/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/acceptable-double-check-detector-assemblies/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/acceptable-double-check-detector-assemblies/data.csv"]
