import requests
r = requests.get("http://www.nyc.gov/html/tlc/downloads/excel/current_medallion_drivers_ad_complete.xls")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/yellow-medallion-taxicabs-drivers-who-have-completed-passenger-assistance-training/data.xls", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/yellow-medallion-taxicabs-drivers-who-have-completed-passenger-assistance-training/data.xls"]
