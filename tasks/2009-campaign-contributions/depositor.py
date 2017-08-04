import requests
r = requests.get("https://data.cityofnewyork.us/api/views/bbs3-q5us/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2009-campaign-contributions/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2009-campaign-contributions/data.csv"]
