import requests
r = requests.get("http://schools.nyc.gov/NR/rdonlyres/146F83FD-E8D3-4C4C-A89F-594DDAD4CE26/0/2008ExcelD75.zip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-school-survey-2008-district-75/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-school-survey-2008-district-75/data.zip"]
