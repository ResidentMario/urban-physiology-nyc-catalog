import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hfac-j85r/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-senior-news-services-in-nycha-journal/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-senior-news-services-in-nycha-journal/data.csv"]
