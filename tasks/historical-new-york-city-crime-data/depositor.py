import requests
r = requests.get("http://www.nyc.gov/html/nypd/downloads/zip/analysis_and_planning/citywide_historical_crime_data_archive.zip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/historical-new-york-city-crime-data/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/historical-new-york-city-crime-data/data.zip"]
