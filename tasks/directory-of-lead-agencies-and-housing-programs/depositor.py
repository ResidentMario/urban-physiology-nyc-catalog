import requests
r = requests.get("https://data.cityofnewyork.us/api/views/b3qc-c6fh/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-lead-agencies-and-housing-programs/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-lead-agencies-and-housing-programs/data.csv"]
