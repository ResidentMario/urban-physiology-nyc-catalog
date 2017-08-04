import requests
r = requests.get("https://data.cityofnewyork.us/download/s7k9-vr5b/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fiscal-2013-appendices/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fiscal-2013-appendices/data.zip"]
