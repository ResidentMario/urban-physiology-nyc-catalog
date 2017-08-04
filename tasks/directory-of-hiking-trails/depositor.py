import requests
r = requests.get("http://nycgovparks.org/bigapps/DPR_Hiking_001.xml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-hiking-trails/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-hiking-trails/data.xml"]
