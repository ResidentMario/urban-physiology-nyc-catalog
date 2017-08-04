import requests
r = requests.get("http://a841-dotweb01.nyc.gov/datafeeds/Citywide%20Arterials%20Milling%20Paving%20Schedule.xml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/weekly-resurfacing-schedule/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/weekly-resurfacing-schedule/data.xml"]
