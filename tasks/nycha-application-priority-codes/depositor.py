import requests
r = requests.get("https://data.cityofnewyork.us/api/views/2ei9-vg68/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycha-application-priority-codes/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycha-application-priority-codes/data.csv"]
