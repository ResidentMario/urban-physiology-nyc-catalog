import requests
r = requests.get("https://data.cityofnewyork.us/api/views/f4yq-wry5/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/mapped-in-ny-companies/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/mapped-in-ny-companies/data.csv"]
