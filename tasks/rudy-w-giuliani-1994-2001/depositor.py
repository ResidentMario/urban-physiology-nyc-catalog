import requests
r = requests.get("https://data.cityofnewyork.us/download/wchz-a6hh/application%2Fx-msaccess")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/rudy-w-giuliani-1994-2001/data.mdb", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/rudy-w-giuliani-1994-2001/data.mdb"]
