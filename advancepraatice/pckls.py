import pickle

# Original data should be a dictionary, not a JSON string
data = {
    "id": 1,
    "name": "yeswanth",
    "age": 25,
    "city": "bengalaru",
    "address": {
        "street": "street1",
        "city": "bengalaru",
        "state": "karnataka",
        "zipcode": "6322312"
    }
}

# Serializing data to bytes object
pdata = pickle.dumps(data)
print(type(pdata))  # Should print: <class 'bytes'>

# Deserializing data back to dictionary
data2 = pickle.loads(pdata)
print(type(data2))  # Should print: <class 'dict'>

# Writing data to a pickle file in binary mode
# with open('use33r.pickle', 'wb') as fh:
#     if fh.writable():
#         pickle.dump(data, fh)
