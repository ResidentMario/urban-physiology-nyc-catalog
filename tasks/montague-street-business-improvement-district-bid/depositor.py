import requests
r = requests.get("https://data.cityofnewyork.us/api/views/5e24-x4wa/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/montague-street-business-improvement-district-bid/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/montague-street-business-improvement-district-bid/data.csv"]
