import json

userdata={
    "id":1,
    "name":"yeswanth",
    "age":25,
    "city":"bengalaru",
    "address":{
        "street":"street1",
        "city":"bengalaru",
        "state":"karnataka",
        "zipcode":"6322312"
    }
}

try:
    with open("user.json",'w') as fh:
        if fh.writable():
            json.dump(userdata,fh)
            print("Data is written to file")
except Exception as e:
    print(e)

