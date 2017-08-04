import requests
r = requests.get("https://data.cityofnewyork.us/api/views/y6fv-k6p7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dcla-programs-funding/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dcla-programs-funding/data.csv"]
