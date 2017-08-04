import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8fei-z6rz/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/weights-measures-and-other-tests/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/weights-measures-and-other-tests/data.csv"]
