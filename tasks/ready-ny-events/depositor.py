import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hyur-qpyf/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ready-ny-events/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ready-ny-events/data.csv"]
