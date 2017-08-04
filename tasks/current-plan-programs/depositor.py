import requests
r = requests.get("https://data.cityofnewyork.us/api/views/bjmk-35w5/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/current-plan-programs/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/current-plan-programs/data.csv"]
