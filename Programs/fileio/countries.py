# print total no of country details
import json

with open("countries.json",encoding="utf-8") as f:
    data=json.load(f)
print(len(data))

# print lang of Ukraine

lang_ukraine=[lang["languages"] for lang in data if lang["name"]=="Ukraine"]
print(lang_ukraine[0])

# print currency in china

currency_china=[cur["currencies"] for cur in data if cur["name"]=="China"]
print(currency_china[0])

# print population of india

india_popu=[p["population"] for p in data if p["name"]=="India"]
print(india_popu)

