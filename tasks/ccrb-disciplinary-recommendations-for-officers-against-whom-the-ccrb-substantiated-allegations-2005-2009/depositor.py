import requests
r = requests.get("https://data.cityofnewyork.us/api/views/jabk-zf7i/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-disciplinary-recommendations-for-officers-against-whom-the-ccrb-substantiated-allegations-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-disciplinary-recommendations-for-officers-against-whom-the-ccrb-substantiated-allegations-2005-2009/data.csv"]
