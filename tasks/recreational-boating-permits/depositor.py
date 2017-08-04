import requests
r = requests.get("https://data.cityofnewyork.us/api/views/idfb-y78n/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/recreational-boating-permits/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/recreational-boating-permits/data.csv"]
