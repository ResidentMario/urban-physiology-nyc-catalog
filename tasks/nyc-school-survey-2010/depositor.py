import requests
r = requests.get("http://schools.nyc.gov/NR/rdonlyres/4C258C57-05CC-4A69-8E99-C3EA4A5E61D9/0/2010SurveyData.zip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-school-survey-2010/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-school-survey-2010/data.zip"]
