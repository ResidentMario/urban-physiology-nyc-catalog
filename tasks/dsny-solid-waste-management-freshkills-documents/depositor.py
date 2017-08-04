import requests
r = requests.get("https://data.cityofnewyork.us/api/views/yv6j-r66f/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dsny-solid-waste-management-freshkills-documents/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dsny-solid-waste-management-freshkills-documents/data.csv"]
