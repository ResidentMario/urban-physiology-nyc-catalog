import requests
r = requests.get("https://data.cityofnewyork.us/api/views/4tqt-y424/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/drivers-and-attendants/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/drivers-and-attendants/data.csv"]
