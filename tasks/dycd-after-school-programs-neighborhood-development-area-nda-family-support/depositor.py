import requests
r = requests.get("https://data.cityofnewyork.us/api/views/chv4-k4fa/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-neighborhood-development-area-nda-family-support/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-neighborhood-development-area-nda-family-support/data.csv"]
