import requests
r = requests.get("https://data.cityofnewyork.us/api/views/sefr-5pmx/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-case-closings-by-type/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-case-closings-by-type/data.csv"]
