import requests
r = requests.get("http://schools.nyc.gov/NR/rdonlyres/623678D2-94D6-45FC-B970-BF1DC1660940/0/2009SurveyData.zip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-school-survey-2009/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-school-survey-2009/data.zip"]
