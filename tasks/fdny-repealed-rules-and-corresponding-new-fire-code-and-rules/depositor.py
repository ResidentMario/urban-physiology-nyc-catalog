import requests
r = requests.get("https://data.cityofnewyork.us/api/views/isrj-349k/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fdny-repealed-rules-and-corresponding-new-fire-code-and-rules/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fdny-repealed-rules-and-corresponding-new-fire-code-and-rules/data.csv"]
