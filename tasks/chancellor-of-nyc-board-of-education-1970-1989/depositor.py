import requests
r = requests.get("https://data.cityofnewyork.us/download/w7es-2nrk/application%2Fx-msaccess")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/chancellor-of-nyc-board-of-education-1970-1989/data.mdb", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/chancellor-of-nyc-board-of-education-1970-1989/data.mdb"]
