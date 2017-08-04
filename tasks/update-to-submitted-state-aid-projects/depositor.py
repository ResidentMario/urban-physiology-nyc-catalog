import requests
r = requests.get("https://data.cityofnewyork.us/api/views/gk83-aa6y/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/update-to-submitted-state-aid-projects/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/update-to-submitted-state-aid-projects/data.csv"]
