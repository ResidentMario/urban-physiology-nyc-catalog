import requests
r = requests.get("https://data.cityofnewyork.us/api/views/k3qa-jvkc/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-nda-family-literacy/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-nda-family-literacy/data.csv"]
