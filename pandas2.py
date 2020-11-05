import pandas as pd

js = {
    "name": ["Pratik Sharma", "Surakshya Ghimire"],
    "phonenumber": ["+15109358632", "+15102669867"],
    "address": ["San Francisco Bay Area", "San Lorenzo"]
}

data = pd.DataFrame(js)
print(data)
print(data[(data['address'] == "San Lorenzo")])
