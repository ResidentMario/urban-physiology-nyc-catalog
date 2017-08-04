import requests
r = requests.get("https://data.cityofnewyork.us/api/views/2enn-s52j/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/adult-family-health-plus-levels/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/adult-family-health-plus-levels/data.csv"]
