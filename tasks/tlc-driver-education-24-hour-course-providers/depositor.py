import requests
r = requests.get("https://data.cityofnewyork.us/api/views/wzur-rhz9/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tlc-driver-education-24-hour-course-providers/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tlc-driver-education-24-hour-course-providers/data.csv"]
