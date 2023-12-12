            # Math Basic:
# Addition
add = 10 + 15

# Subtraction
sub = 10 - 15

# Multiplication
mul = 10 * 15

# Division
div = 10 / 4

# Floor Division (rounded down to the nearest whole number)
floor = 10 // 4

# Modulus (remainder of division)
mod = 10 % 2

# Exponentiation
expo = 2 ** 3

# print(add, sub, mul, div, floor, mod, expo)

            # Math Module: import math
import math
# Square root
sqrt = math.sqrt(16)

# Absolute value
ab = math.fabs(-10)

# Factorial
fac = math.factorial(5)

# Trigonometric functions (radians)
result = math.sin(math.radians(30))

# Logarithmic functions
result = math.log(100, 10)  # log base 10 of 100

# Constants
pi_value = math.pi
e_value = math.e


# print(sqrt, ab, fac, pi_value, e_value)

            # Random Module: import random
import random 

# Random float in the range [0.0, 1.0)
random = random.random()

# Random integer in the range [start, end]
# r_int = random.randint(1,10)

# print(random, r_int)

            # Collections Module:  import collections
import collections
# Defaultdict 
my_dict = collections.defaultdict(int)

# Counter 
my_list = [1, 2, 3, 1, 2, 1, 3, 4]
count = collections.Counter(my_list)

# print(my_dict["test"], count)

            # Iterate tools Module:  import itertools
import itertools
# Count
# for i in itertools.count(0, 1):
#     if i % 2 == 0: print(str(i) +  " - Even")
#     else: print(i)
#     if i >= 1000:
#         break 


# Cycle 
colors = itertools.cycle(["red", "green","tomato"])

# for i in itertools.count(0,1):
#     if i >= 25: break
#     print(next(colors)) 

# Repeat 
my_list = itertools.repeat("This", 10)
# print(list(my_list))

# Chain 
list1 = [1, 2, 3, 4]
tuple1 = ('a', 'b', 'c','d')
strs1 = "THIS"

combined = itertools.chain(list1, tuple1, strs1)
# print(combined)
# print(list(combined))

# Combinations 
items =  [1, 2, 3, 4]
# for combo in itertools.combinations(items,2):
#     print(combo)

# Permutations 
# for perm in itertools.permutations(items, 2):
#     print(perm)
