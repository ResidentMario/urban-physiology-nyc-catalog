import requests
r = requests.get("https://data.cityofnewyork.us/api/views/mkxg-y5uc/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-offensive-language-allegations-2008/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-offensive-language-allegations-2008/data.csv"]
