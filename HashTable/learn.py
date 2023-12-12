# A hash table, also known as a hash map, is a data structure that allows efficient insertion, deletion, and retrieval of elements.

# Handling Collisions:
# In hash tables, collisions can occur when multiple keys hash to the same index. Python dictionaries handle collisions using a technique called open addressing.

            # Creating Dicts 
# Creating an empty dictionary
dict_ = {}
dict_["key"] = "Value"

# Creating a dictionary with initial values
from collections import defaultdict 
dict_default = defaultdict(int)

            # Accessing and Modifying Elements
# Accessing a value by key
value = dict_default["notKey"] # Default value will be returned 

# Modifying a value
# print(dict_["key"])
dict_["key"] = "New Value"
# print(dict_["key"])

# Adding a new key-value pair
dict_["key2"] = "Value2"
dict_["key3"] = "Value3"
dict_["key4"] = "Value4"

# Removing a key-value pair
del dict_["key2"]

# print(dict_)

            # Methods
# Getting all keys and values
keys = dict_.keys()
values = dict_.values()

# print(keys)
# print(values)

# Checking if a key is in the dictionary
check = "key" in dict_.keys()

# Getting a value with a default if the key doesn't exist
value = dict_.get("key2", 1)

# print(value)

# Removing and returning a key-value pair
popped = dict_.popitem()
# print(popped)
print(dict_)

            # Iterating the Dicts
# Iterating through keys
# for key in dict_:
#     print(key)

# Iterating through key-value pairs
# for key, value in dict_.items():
#     print(key, value)
