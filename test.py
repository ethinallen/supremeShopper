import json

# open the json file
with open('details.json') as data:
    data = json.load(data)

# print the product productType
print(data['productType'])
