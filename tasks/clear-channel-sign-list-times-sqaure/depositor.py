import requests
r = requests.get("https://data.cityofnewyork.us/api/views/wjtn-s4z7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/clear-channel-sign-list-times-sqaure/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/clear-channel-sign-list-times-sqaure/data.csv"]
