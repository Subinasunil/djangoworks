# print total no of country details
import json

with open("countries.json",encoding="utf-8") as f:
    data=json.load(f)
print(len(data))

def get_country_data(country_name):
    return [country for country in data if country["name"].lower().startswith(country_name)]

# print lang of Ukraine

lang_ukraine=[lang["languages"] for lang in data if lang["name"]=="Ukraine"]
for lan in lang_ukraine[0]:
    print(lan["name"])


# print currency in china

currency_details=[cur["currencies"] for cur in data if cur["name"].startswith("Palestine")]
currency=[cur["name"] for cur in currency_details[0]]
print(currency)

# print population of india

india_popu=[p["population"] for p in data if p["name"]=="India"]
print(india_popu)


aust_data=get_country_data("austria")
print(aust_data[0].get("borders"))
india_data=get_country_data("india")
print(india_data[0].get("borders"))


country_data=get_country_data("ukra")
country_borders=country_data[0].get("borders")
sharing_borders=[country.get("name") for country in data if country["alpha3Code"] in country_borders]
print(sharing_borders)

highest_populated=max(data,key=lambda d:d.get("population"))
print(highest_populated["name"])

lowest_populated=min(data,key=lambda d:d.get("population"))
print(lowest_populated["name"])