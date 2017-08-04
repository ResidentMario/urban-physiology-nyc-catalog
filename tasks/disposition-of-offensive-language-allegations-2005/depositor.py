import requests
r = requests.get("https://data.cityofnewyork.us/api/views/s5ne-bpvg/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-offensive-language-allegations-2005/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-offensive-language-allegations-2005/data.csv"]
