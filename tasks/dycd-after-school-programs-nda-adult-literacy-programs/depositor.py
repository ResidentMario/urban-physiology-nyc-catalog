import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ia9u-k3t3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-nda-adult-literacy-programs/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-nda-adult-literacy-programs/data.csv"]
