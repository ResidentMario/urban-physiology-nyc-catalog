import requests
r = requests.get("https://data.cityofnewyork.us/api/views/3h6b-pt5u/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/total-crime-index-for-the-nations-largest-cities/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/total-crime-index-for-the-nations-largest-cities/data.csv"]
