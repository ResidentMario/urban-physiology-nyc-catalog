import requests
r = requests.get("https://data.cityofnewyork.us/api/views/24nr-gahi/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/five-year-plan-summary-by-borough-and-capital-categories/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/five-year-plan-summary-by-borough-and-capital-categories/data.csv"]
