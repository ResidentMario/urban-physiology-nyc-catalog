import requests
r = requests.get("https://data.cityofnewyork.us/api/views/i9pf-sj7c/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doe-high-school-programs-2013-2014/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doe-high-school-programs-2013-2014/data.csv"]
