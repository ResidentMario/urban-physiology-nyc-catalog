import requests
r = requests.get("https://data.cityofnewyork.us/api/views/432v-a7hc/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/population-of-selected-asian-race-subgroups-in-new-york-city-by-borough/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/population-of-selected-asian-race-subgroups-in-new-york-city-by-borough/data.csv"]
