import requests
r = requests.get("http://nycgovparks.org/bigapps/DPR_RecreationCenter_001.xml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-recreation-centers/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-recreation-centers/data.xml"]
