# Counting is a common operation in programming, and it involves keeping track of the occurrences of elements in a collection.

# Using the Counter class (from the collections module):

# Using Dictionaries for Manual Counting:
my_list = [1, 2, 3, 1, 2, 1, 3, 4]
count_dict = {}


for num in my_list:
    count_dict[num] = count_dict.get(num, 0) + 1

# print(count_dict)

    # Using defaultdict for Default Values:
from collections import defaultdict, Counter  
count_dict = defaultdict(int)

for num in my_list:
    count_dict[num] += 1

# print(count_dict)


# Counting Characters in a String:
string = "programming"
counter = Counter(string)

r_count = counter["r"]
# print(r_count)

# Using count method for Lists:
from itertools import count 
list_ = [1, 2, 3, 1, 2, 1, 3, 4]

count_1 = list_.count(1)
# print(count_1)