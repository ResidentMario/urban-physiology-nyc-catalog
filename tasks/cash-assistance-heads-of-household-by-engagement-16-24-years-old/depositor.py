import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6ayi-u3p7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/cash-assistance-heads-of-household-by-engagement-16-24-years-old/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/cash-assistance-heads-of-household-by-engagement-16-24-years-old/data.csv"]
