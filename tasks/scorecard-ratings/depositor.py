import requests
r = requests.get("https://data.cityofnewyork.us/api/views/rqhp-hivt/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/scorecard-ratings/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/scorecard-ratings/data.csv"]
