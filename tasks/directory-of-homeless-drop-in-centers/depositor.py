import requests
r = requests.get("https://data.cityofnewyork.us/api/views/bmxf-3rd4/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-homeless-drop-in-centers/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-homeless-drop-in-centers/data.csv"]
