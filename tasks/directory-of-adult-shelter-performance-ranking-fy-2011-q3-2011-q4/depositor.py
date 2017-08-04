import requests
r = requests.get("https://data.cityofnewyork.us/api/views/jhn3-4vdj/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-adult-shelter-performance-ranking-fy-2011-q3-2011-q4/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-adult-shelter-performance-ranking-fy-2011-q3-2011-q4/data.csv"]
