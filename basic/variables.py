# 1. Data type -> single value
    # integers
    # float
    # string 
    # boolean

a = 5
b = 6.6
c = "Hello"
d = True

print("a", b, c, d)
print(type(a), type(b), type(c), type(d))

# 2. Data Structures
    # list []
    # tuple () -> immutable (cannot change by adding item, etc.) -> can do everything as list like retrieving values and calculations but cannot change and append
    # dictionary {}
    # sets {}

# LISTS

e = ["Apple", 9, 8.5, a, [5, 6, 7, 8, [b, c]]] # has 5 variables
print(len(e)) # will print length of list
print(e[0]) # number in square brackets indicates the index or the value in a list
print(e)

# List Slicing:
print(e[0:3]) # will print all values from 0 (inclusive) to 3 exclusive, don't need start or end to start from beginning and go to finish
print(e[-1]) # negative values indicate going from end
print(e[-3:]) # will print the last 3 elements of array
print(e[-4:-2]) # will print third and fourth to last (don't know how long it is)

# To insert values to a list
e.append(25) # insert at the end
print(e)
e.insert(3, 'World') # insert as index 3
print(e)

# To delete values
e.pop(1) # delete index 2
print(e)
e.remove(9) # will delete the first occurrence of that value in the list
print(e)
e[0] = "Orange" # index being replaced
print(e)

# TUPLES
f = (7, 8, 9, 10.5, "Class")
f = (7, 8, 9, 10.5, "Class", 5) # must create new tuple to change it
print(f[3]) # all other aforementioned operations also work

# DICTIONARY -> key value pairs
h = {3:5, 4:6, 7:8, "ello":5, 4:10}
print(h)
print(h[3]) # will print the value for key 3 which is 5
print(h.get("ello"))
print(h[4]) # will print the latest value

h[7] = "house" 
print(h[7])

h[5] = 100 # will add value to the end of dictionary
print(h)

h.update({7:16, 9:200})  # will update a key value pair and add one
print(h)

print(h.keys()) #will print all the keys, cannot print specific keys

# SET
g = {2, 2, 1, "glass", 5, 1, "Hi", "mermaid"}
print(g) # INDEXING DOES NOT WORK, prints in order (its own order); only keeps unique values

g.add(3) # 3 will be inserted in the list in order
print(g)

g.add(5) # 5 is a duplicate and won't be inserted
print(g)

g.remove(5) # only stores 1 so doesn't matter how many 5's there are in list
print(g)

# ASSIGNMENT 1

# Create a list of 5 fruits. Perform the following operations:
z = ["Apple", "Orange", "Banana", "Mango", "Guava"]

# Add a fruit to the end
z.append("Strawberry")
print(z)

# Remove the 2nd item
z.pop(1)
print(z)

# Sort the list
z = sorted(z)

# Print the final list
print(z)

# ASSIGNMENT 2

# Create a dictionary with the following keys:

# "name": your name

# "age": your age

# "skills": list of 3 programming languages

y = {"name": "Maanvitha", "age": 15, "skills":["Python", "Java", "R"]}

# Do the following:

# Add a new key "city"
y.update({"city": "Sunnyvale"})
print(y)

# Update "age" by adding 1
y["age"] += 1

# Delete the key "skills"
y.pop("skills")

# Print the final dictionary
print(y)

# ASSIGNMENT 3

# Write a program that:

# Takes a list of integers as input

integer_list = list(input("Enter integer list separated by spaces: "))

# Calculates the sum and average of the numbers

add integer_list[]

# ASSIGNMENT 4:

# Given a list of words, count how many times each word occurs.
words = ["Ginny", "Georgia", "Georgia", "Hunter", "Max", "Ginny", "Ginny", " Zion", "Max", "Austin", "Ginny"]

# store them in dictionary -> el = element
dictionary = {}
for el in words:
    if el in dictionary:
        dictionary[el] += 1
    else:
        dictionary[el] = 1

print(dictionary)

# ASSIGNMENT 5

# Create a dictionary called employee with keys: "name", "id", "department", and "salary". Print each key-value pair.

employee = {"name":"Maanvitha", "id":565, "department":"Business", "salary":"$300 billion"}
print(employee)
