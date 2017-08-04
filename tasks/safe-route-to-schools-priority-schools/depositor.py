import requests
r = requests.get("https://data.cityofnewyork.us/api/views/pc34-d3sx/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/safe-route-to-schools-priority-schools/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/safe-route-to-schools-priority-schools/data.csv"]
