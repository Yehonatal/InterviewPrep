            # Creating and Access 
# Creating an empty list
l = []
# Creating a list with elements
list_ = [0, 1, 2, 3, 4, 5]

# Accessing elements by index
one = list_[0]


            # Modifying Lists
# Appending an element
list_.append(6)

# Extending with another list
list_2 = [7, 8, 9]
list_.extend(list_2)

# Inserting an element at a specific index
list_2.insert(0, "666")

# Removing an element by value
list_2.remove(9)

# Removing an element by index
popped = list_2.pop()

# Slicing a sublist
list_sub = list_[0:5]

# Slicing with step
list_even = list_[::2]

# Concatenating lists
list_ += [100]

# Repeating a list
list_ *= 2

# print(popped)
# print(list_sub)
# print(list_2)
# print(list_even)
# print(list_)
            # Functions in List 
# Finding length
length = len(list_)

# Finding maximum and minimum
max_ = max(list_)

# Comprehension and Iteration 
even = [x for x in list_ if x % 2 == 0]

# Iterating through elements
# for num in list_:
#     print(num)

# Iterating with index
for i, num in enumerate(list_):
    print(i, num)


# Creating a new list using list comprehension
even = [x for x in list_ if x % 2 == 0]
