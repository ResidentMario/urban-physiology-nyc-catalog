import requests
r = requests.get("http://www.nycgovparks.org/bigapps/DPR_Inspection_001.xml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/parks-inspections-data/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/parks-inspections-data/data.xml"]
