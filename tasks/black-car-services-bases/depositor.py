import requests
r = requests.get("http://www.nyc.gov/html/tlc/downloads/excel/current_black_car_bases.xls")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/black-car-services-bases/data.xls", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/black-car-services-bases/data.xls"]
