import requests
r = requests.get("https://data.cityofnewyork.us/api/views/26kp-bgdh/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-state-english-language-arts-ela-exam/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-state-english-language-arts-ela-exam/data.csv"]
