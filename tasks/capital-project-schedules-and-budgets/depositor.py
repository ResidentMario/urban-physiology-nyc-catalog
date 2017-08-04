import requests
r = requests.get("https://data.cityofnewyork.us/api/views/2xh6-psuq/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/capital-project-schedules-and-budgets/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/capital-project-schedules-and-budgets/data.csv"]
