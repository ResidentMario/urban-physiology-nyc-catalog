import requests
r = requests.get("https://data.cityofnewyork.us/api/views/j8p3-8ufc/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dcla-programs-funding-for-fy2010/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dcla-programs-funding-for-fy2010/data.csv"]
