import requests
r = requests.get("https://data.cityofnewyork.us/api/views/n3p6-zve2/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doe-high-school-directory-2014-2015/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doe-high-school-directory-2014-2015/data.csv"]
