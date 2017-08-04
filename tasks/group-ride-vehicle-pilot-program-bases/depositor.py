import requests
r = requests.get("http://www.nyc.gov/html/tlc/downloads/excel/current_group_ride_bases.xls")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/group-ride-vehicle-pilot-program-bases/data.xls", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/group-ride-vehicle-pilot-program-bases/data.xls"]
