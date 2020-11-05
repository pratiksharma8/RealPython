def map_by_name(arr):
    new = [x["name"] for x in arr]
    print(new)


pets = [
    {"type": "dog", "name": "Rolo"},
    {"type": "cat", "name": "Sunny"},
    {"type": "rat", "name": "Saki"},
    {"type": "dog", "name": "Finn"},
    {"type": "cat", "name": "Buffy"}
]

countries = [
    {"name": "Japan", "continent": "Asia"},
    {"name": "Hungary", "continent": "Europe"},
    {"name": "Kenya", "continent": "Africa"},
]
map_by_name(pets)
map_by_name(countries)
