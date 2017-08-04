import requests
r = requests.get("https://data.cityofnewyork.us/api/views/2t2c-qih9/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/full-time-and-full-time-equivalent-staffing-levels/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/full-time-and-full-time-equivalent-staffing-levels/data.csv"]
