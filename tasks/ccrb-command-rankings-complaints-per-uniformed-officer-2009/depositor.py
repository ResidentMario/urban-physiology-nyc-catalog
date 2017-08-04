import requests
r = requests.get("https://data.cityofnewyork.us/api/views/83kr-sbhe/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-command-rankings-complaints-per-uniformed-officer-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-command-rankings-complaints-per-uniformed-officer-2009/data.csv"]
