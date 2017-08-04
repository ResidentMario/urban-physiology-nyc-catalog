import requests
r = requests.get("https://data.cityofnewyork.us/api/views/pyif-r8qe/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-beacon-satellite-at-nycha-programs/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-beacon-satellite-at-nycha-programs/data.csv"]
