import requests
r = requests.get("https://data.cityofnewyork.us/api/views/grnn-mvqe/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-work-and-family-leave-survey-wfls-2014/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-work-and-family-leave-survey-wfls-2014/data.csv"]
