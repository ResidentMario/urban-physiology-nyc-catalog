import requests
r = requests.get("https://data.cityofnewyork.us/api/views/m64p-r9hk/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/certified-asbestos-investigator/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/certified-asbestos-investigator/data.csv"]
