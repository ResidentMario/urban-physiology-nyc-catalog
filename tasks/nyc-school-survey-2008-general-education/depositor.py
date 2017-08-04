import requests
r = requests.get("http://schools.nyc.gov/NR/rdonlyres/EB281589-6F2B-42E5-A0AD-13C8CE2E8CDD/0/2008excel.zip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-school-survey-2008-general-education/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-school-survey-2008-general-education/data.zip"]
