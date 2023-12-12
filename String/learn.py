            # Basic String Operations:

# Concatenation
conc = "string" + " Concatenation "

# Length of a string
length = len(conc)

# Accessing characters by index
char = conc[0]

# Slicing
sliced = conc[::-1]

# String repetition
rep = conc[:6] * 2

# Checking substring presence
check = "string" in conc 

# print(conc, length, char, sliced, rep, check)

            # String Methods 
# Conversion to lowercase and uppercase
upper = conc.upper()
lower = conc.lower()

# Finding and replacing substrings
find = conc.find("string")
change = conc.replace("string", "notString")

# Splitting and joining
split = conc.split()

# Stripping whitespace
conc = conc.strip()

# print(upper, lower)
# print(find)
# print(change)
# print(split)
# print(conc)

            # String Formatting
# F-string formatting (Python 3.6+)
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."


# Format method
formatted_string = "My name is {} and I am {} years old.".format(name, age)

            # Regular Expressions
# Matching a pattern