import requests
r = requests.get("https://www.nycgovparks.org/bigapps/DPR_Pools_indoor_001.xml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-indoor-swimming-pools/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-indoor-swimming-pools/data.xml"]
