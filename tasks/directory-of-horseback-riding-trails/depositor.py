import requests
r = requests.get("http://nycgovparks.org/bigapps/DPR_Horseback_001.xml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-horseback-riding-trails/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-horseback-riding-trails/data.xml"]
