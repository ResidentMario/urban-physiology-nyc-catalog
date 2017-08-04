import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hjnm-89hx/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/family-assistance-fa-recipients/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/family-assistance-fa-recipients/data.csv"]
