import requests
r = requests.get("http://www.nycgovparks.org/bigapps/DPR_Bocce_001.xml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-bocce-courts/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-bocce-courts/data.xml"]
