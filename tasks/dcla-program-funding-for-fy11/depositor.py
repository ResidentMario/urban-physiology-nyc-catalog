import requests
r = requests.get("https://data.cityofnewyork.us/api/views/rskq-5bfv/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dcla-program-funding-for-fy11/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dcla-program-funding-for-fy11/data.csv"]
