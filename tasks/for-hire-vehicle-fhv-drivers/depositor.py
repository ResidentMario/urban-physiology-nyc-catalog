import requests
r = requests.get("http://www.nyc.gov/html/tlc/downloads/excel/current_fhv_drivers.xls")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/for-hire-vehicle-fhv-drivers/data.xls", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/for-hire-vehicle-fhv-drivers/data.xls"]
