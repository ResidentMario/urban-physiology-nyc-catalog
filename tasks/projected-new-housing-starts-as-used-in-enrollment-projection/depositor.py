import requests
r = requests.get("https://data.cityofnewyork.us/api/views/pa5t-ktd3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/projected-new-housing-starts-as-used-in-enrollment-projection/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/projected-new-housing-starts-as-used-in-enrollment-projection/data.csv"]
