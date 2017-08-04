import requests
r = requests.get("https://data.cityofnewyork.us/api/views/y7z5-rhh5/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-family-shelter-performance-ranking-fy-2012-q4-and-2013-q1/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-family-shelter-performance-ranking-fy-2012-q4-and-2013-q1/data.csv"]
