import requests
r = requests.get("http://nyc.gov/html/dpr/nycbigapps/DPR_marinas_001.xml")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-boating-and-marinas/data.xml", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-boating-and-marinas/data.xml"]
