import requests
r = requests.get("https://data.cityofnewyork.us/api/views/rbvx-jqnh/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fcrc-annual-concession-plan-franchises/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fcrc-annual-concession-plan-franchises/data.csv"]
