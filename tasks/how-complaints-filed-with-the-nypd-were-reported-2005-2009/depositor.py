import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ihvw-cp8d/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/how-complaints-filed-with-the-nypd-were-reported-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/how-complaints-filed-with-the-nypd-were-reported-2005-2009/data.csv"]
