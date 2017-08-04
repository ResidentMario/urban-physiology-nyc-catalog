import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ut9y-2ptp/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-nda-educational-high-school-progams/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-nda-educational-high-school-progams/data.csv"]
