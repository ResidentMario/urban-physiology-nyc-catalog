import requests
r = requests.get("https://data.cityofnewyork.us/api/views/yj3u-pw36/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/borough-enrollment-centers-additional-ways-to-graduate/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/borough-enrollment-centers-additional-ways-to-graduate/data.csv"]
