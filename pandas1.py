import pandas as pd

l1 = [1, 2, 3, 4, 5]
data1 = pd.DataFrame(l1)
print(data1)

dt1 = {
    'fruit_name': ['apple', 'mango', 'orange'],
    'count': ['12', '23', '43']
}
data2 = pd.DataFrame(dt1)
print(data2)