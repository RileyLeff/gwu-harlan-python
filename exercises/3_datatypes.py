# the values assigned to a variable are of a certain "data type"
# this relates to how objects are stored internally as binary 1s and 0s: riley can show this on a whiteboard if people are interested

# here are some common, built-in types in python:

# str ---> text data
var1 = "this is a string" # str

# numbers
var2 = 25 # int
var3 = 25.0 # float

# bool ---> True or False, ALWAYS CAPITALIZED LIKE THAT
var4 = True # bool
var5 = False # bool

# empty / missing value
var6 = None # none!

# multi-value types
var7 = [0,1,2,3,4] # list - mutable
var8 = (0,1,2) # tuple - immutable
var9 = set(0,1,2,3) # set --> can only contain one of each of its elements!

# dict, aka dictionary aka hashmap
# stores a key (a name) alongside a value (can be pretty much anything)
# very powerful
var10 = {'riley': 2, 'keryn': 39, 'tommy': 500} # dict

# how to check the type of an object
type_of_var10 = type(var8)
print(type_of_var10)

# there are handy functions to convert between types:
a = 1.0 # x is a float
a = int(a)
a = str(a)
b = [a] # wrapping in brackets is the same as converting to list
c = list(a)
# try printing out b and c to confirm!

# tuple() and set() also available

c = {a:'cool'} # wrapping in curlies is how to create a dict

# uncomment these lines to try converting x (float) to x (str)
# x = str(x)
# print(x)

# exercises:

# 1. what would this code print out if uncommented?

# x = 1.0
# x = x + x
# y = str(x)
# y = y + y
# z = [x,y]
# print(z)


# 2. lists and tuples can contain multiple objects. do all the objects in the list/tuple have to be of the same type?


# 3. what happens if you have a list with repeated elements, and you convert it into a set? 
# For example: try it with this list
# my_list = [0,0,0,0,1,2,3,3,3,3,3,4,5,6]
# remember, the function to create a new set (or convert something into a set) is set(name_of_object)




