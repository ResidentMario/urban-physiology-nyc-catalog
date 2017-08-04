import requests
r = requests.get("http://www.nyc.gov/html/tlc/downloads/excel/for_hire_vehicles_open_summonses.xls")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/open-summonses-active-for-hire-vehicle-fhv-owners/data.xls", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/open-summonses-active-for-hire-vehicle-fhv-owners/data.xls"]
