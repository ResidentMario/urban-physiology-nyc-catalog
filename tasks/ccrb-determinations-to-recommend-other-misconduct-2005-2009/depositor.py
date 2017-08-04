import requests
r = requests.get("https://data.cityofnewyork.us/api/views/v3f6-2e7z/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-determinations-to-recommend-other-misconduct-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-determinations-to-recommend-other-misconduct-2005-2009/data.csv"]
