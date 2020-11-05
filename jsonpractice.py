import json

# Data to be written
dictionary = {
    "name": "Pratik Sharma",
    "phonenumber": "+15109358632",
    "address": "San Francisco Bay Area"
}


# Writing to sample.json
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile, indent=4)

with open("sample.json", "r") as readfile:
    json_object = json.load(readfile)

    print(json_object)
