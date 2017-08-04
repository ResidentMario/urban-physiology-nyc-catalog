import requests
r = requests.get("https://data.cityofnewyork.us/api/views/s7yj-m732/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-department-of-education-job-titles/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-department-of-education-job-titles/data.csv"]
