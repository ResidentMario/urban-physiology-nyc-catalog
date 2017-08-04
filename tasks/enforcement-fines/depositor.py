import requests
r = requests.get("https://data.cityofnewyork.us/api/views/p39r-nm7f/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/enforcement-fines/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/enforcement-fines/data.csv"]
