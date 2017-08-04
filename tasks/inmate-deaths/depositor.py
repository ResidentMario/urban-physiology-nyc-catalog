import requests
r = requests.get("https://data.cityofnewyork.us/api/views/f64t-5yiv/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inmate-deaths/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inmate-deaths/data.csv"]
