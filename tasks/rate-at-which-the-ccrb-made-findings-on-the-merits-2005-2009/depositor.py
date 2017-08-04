import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6wkw-kjx4/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/rate-at-which-the-ccrb-made-findings-on-the-merits-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/rate-at-which-the-ccrb-made-findings-on-the-merits-2005-2009/data.csv"]
