import requests
r = requests.get("http://nycgovparks.org/bigapps/DPR_ParkClosure_001.xml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/park-closure-notifications/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/park-closure-notifications/data.xml"]
