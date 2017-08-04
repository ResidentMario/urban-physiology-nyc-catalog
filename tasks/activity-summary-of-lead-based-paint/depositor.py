import requests
r = requests.get("https://data.cityofnewyork.us/api/views/996g-i4kh/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/activity-summary-of-lead-based-paint/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/activity-summary-of-lead-based-paint/data.csv"]
