import requests
r = requests.get("https://data.cityofnewyork.us/api/views/qvir-knu3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doe-high-school-performance-directory-2016/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doe-high-school-performance-directory-2016/data.csv"]
