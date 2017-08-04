import requests
r = requests.get("http://www.hraadvisors.com/wp-content/uploads/2014/04/NYC_Tech_Ecosystem_Data1.zip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-tech-ecosystem-report-data/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-tech-ecosystem-report-data/data.zip"]
