import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ph76-k6qa/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/drinking-fountains/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/drinking-fountains/data.csv"]
