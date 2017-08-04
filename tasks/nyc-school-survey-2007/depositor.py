import requests
r = requests.get("http://schools.nyc.gov/NR/rdonlyres/3C9B6404-D3C3-49D7-8FA8-36AC191BC328/26549/surveyaccess_1011092.xls")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-school-survey-2007/data.xls", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-school-survey-2007/data.xls"]
