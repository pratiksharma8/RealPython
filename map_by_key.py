def map_by_key(arr, key):
    new = [x[key] for x in arr]
    print(new)


locations = [
    {"city": "New York City", "state": "New York", "coast": "East"},
    {"city": "San Francisco", "state": "California", "coast": "West"},
    {"city": "Portland", "state": "Oregon", "coast": "West"},
]

map_by_key(locations, "state")  #: ["New York", "California", "Oregon"]

map_by_key(locations, "city")  #: ["New York City", "San Francisco", "Portland"]
