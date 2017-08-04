import requests
r = requests.get("https://data.cityofnewyork.us/api/views/wwhr-5ven/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/participatory-budgeting-projects/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/participatory-budgeting-projects/data.csv"]
