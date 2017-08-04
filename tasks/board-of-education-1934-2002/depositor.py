import requests
r = requests.get("https://data.cityofnewyork.us/download/bevq-88e4/application%2Fx-msaccess")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/board-of-education-1934-2002/data.mdb", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/board-of-education-1934-2002/data.mdb"]
