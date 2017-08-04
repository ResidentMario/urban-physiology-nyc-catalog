import requests
r = requests.get("https://data.cityofnewyork.us/api/views/656a-faqy/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/grand-street-bid-business-directory/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/grand-street-bid-business-directory/data.csv"]
