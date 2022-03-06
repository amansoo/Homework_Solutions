import pickle

with open('my_data.pkl', 'rb') as md:
    data = pickle.load(md)

for (name, encoding) in data:
    print('Person: {0}'.format(name))
