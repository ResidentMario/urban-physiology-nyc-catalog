import requests
r = requests.get("https://data.cityofnewyork.us/api/views/bjuu-44hx/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/derelict-vehicle-dispositions-vehicles/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/derelict-vehicle-dispositions-vehicles/data.csv"]
