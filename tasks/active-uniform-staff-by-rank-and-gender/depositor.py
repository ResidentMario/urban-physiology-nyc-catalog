import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6dn9-qgma/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/active-uniform-staff-by-rank-and-gender/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/active-uniform-staff-by-rank-and-gender/data.csv"]
