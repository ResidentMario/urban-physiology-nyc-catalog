import requests
r = requests.get("https://data.cityofnewyork.us/api/views/x56h-7iwp/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-unsheltered-street-homeless-to-general-population-ratio-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-unsheltered-street-homeless-to-general-population-ratio-2009/data.csv"]
