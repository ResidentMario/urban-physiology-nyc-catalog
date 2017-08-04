import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8n8g-m3vw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/list-of-translation-services-provided-at-oath/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/list-of-translation-services-provided-at-oath/data.csv"]
