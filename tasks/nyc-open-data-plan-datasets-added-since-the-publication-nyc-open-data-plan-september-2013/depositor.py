import requests
r = requests.get("https://data.cityofnewyork.us/api/views/qnuk-aubm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-open-data-plan-datasets-added-since-the-publication-nyc-open-data-plan-september-2013/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-open-data-plan-datasets-added-since-the-publication-nyc-open-data-plan-september-2013/data.csv"]
