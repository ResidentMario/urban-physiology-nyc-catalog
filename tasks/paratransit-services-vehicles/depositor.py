import requests
r = requests.get("http://www.nyc.gov/html/tlc/downloads/excel/current_paratransit_vehicles.xls")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/paratransit-services-vehicles/data.xls", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/paratransit-services-vehicles/data.xls"]
