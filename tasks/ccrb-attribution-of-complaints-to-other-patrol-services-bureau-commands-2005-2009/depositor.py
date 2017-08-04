import requests
r = requests.get("https://data.cityofnewyork.us/api/views/wudr-qbgm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-attribution-of-complaints-to-other-patrol-services-bureau-commands-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-attribution-of-complaints-to-other-patrol-services-bureau-commands-2005-2009/data.csv"]
