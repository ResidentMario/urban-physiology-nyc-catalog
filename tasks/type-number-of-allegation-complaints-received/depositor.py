import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ngf9-zejg/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/type-number-of-allegation-complaints-received/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/type-number-of-allegation-complaints-received/data.csv"]
