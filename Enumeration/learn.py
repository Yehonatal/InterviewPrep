# Enumeration, often referred to as enumerating or iterating, is the process of going through a collection of items, such as a list or an array, and processing each item one by one.

list_ = ['man', 'woman', 'child']
# Using enumerate
for i, ele in enumerate(list_):
    print(i, ele)

# Enumerating with zip
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]
zipped = list(zip(names, ages))

for i, (name, age) in enumerate(zipped):
    print(i, name, age)


# Using enumerate with Dictionaries
my_dict = {'a': 1, 'b': 2, 'c': 3}

for i, (key, value) in enumerate(my_dict.items()):
    print(i, key, value)

# Enumerating a String
my_string = "Python"

for i, char in enumerate(my_string):
    print(i, char)


# Using enumerate with List Comprehension
list_ = [1, 2, 3, 4, 5]
squared = [num ** 2 for i, num in enumerate(list_)]
print(squared)