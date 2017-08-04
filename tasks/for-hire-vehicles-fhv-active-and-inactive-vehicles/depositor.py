import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8wbx-tsch/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/for-hire-vehicles-fhv-active-and-inactive-vehicles/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/for-hire-vehicles-fhv-active-and-inactive-vehicles/data.csv"]
