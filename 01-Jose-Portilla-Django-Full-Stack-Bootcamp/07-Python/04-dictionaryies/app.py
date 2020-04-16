my_stuff = {
    "key1": "value1",
    "key2": "value2",
    "key3": {
        "123": [1, 2, 3]
    }
}

print(my_stuff["key1"])

print(my_stuff["key3"]["123"][1])

my_stuff["key3"] = "value3"
print(my_stuff)

my_stuff["key4"] = "value4"
print(my_stuff)
