import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ppzj-4i42/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/catch-basin-inspection-and-cleaning-activity/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/catch-basin-inspection-and-cleaning-activity/data.csv"]
