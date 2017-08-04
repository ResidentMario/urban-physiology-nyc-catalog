import requests
r = requests.get("http://www.nyc.gov/html/tlc/downloads/excel/current_community_car_service_vehicles.xls")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/community-car-services-livery-vehicles/data.xls", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/community-car-services-livery-vehicles/data.xls"]
