import requests
r = requests.get("https://data.cityofnewyork.us/api/views/egiq-kmr5/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-attribution-of-complaints-to-patrol-boroughs-and-other-commands-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-attribution-of-complaints-to-patrol-boroughs-and-other-commands-2005-2009/data.csv"]
