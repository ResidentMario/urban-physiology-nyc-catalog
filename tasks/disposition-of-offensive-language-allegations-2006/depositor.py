import requests
r = requests.get("https://data.cityofnewyork.us/api/views/sxxc-x9gg/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-offensive-language-allegations-2006/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-offensive-language-allegations-2006/data.csv"]
