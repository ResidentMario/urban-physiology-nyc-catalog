import requests
r = requests.get("https://data.cityofnewyork.us/api/views/4fif-5bmt/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/acceptable-reduced-pressure-detector-assemblies/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/acceptable-reduced-pressure-detector-assemblies/data.csv"]
