import requests
r = requests.get("https://data.cityofnewyork.us/api/views/y6ih-4ijb/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fdny-fire-rule/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fdny-fire-rule/data.csv"]
