import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ne9f-g6k4/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/lincoln-square-bid-business-list/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/lincoln-square-bid-business-list/data.csv"]
