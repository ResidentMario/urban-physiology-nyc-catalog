import requests
r = requests.get("https://data.cityofnewyork.us/api/views/a2rn-4ju4/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/community-board-applications/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/community-board-applications/data.csv"]
