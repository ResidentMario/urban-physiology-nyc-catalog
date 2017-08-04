import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6246-94tp/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/observations-and-statuses-for-inspections/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/observations-and-statuses-for-inspections/data.csv"]
