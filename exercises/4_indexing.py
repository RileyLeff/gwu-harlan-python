# objects that contain multiple elements, like lists, can be indexed to grab a specific constituent value.
# indexing is done by putting brackets after the variable name
# an index is the position of the element in the list -- first element is 0

my_list = [1,2,3,4,5]
my_list[3] # grab third element of my_list
# note that python indexes from zero!

# you can also grab elements from the end of the list using negative numbers.
# the final element of the list is at position [-1], the second-to-last is [-2], and so on.
my_last_thing = my_list[-1]

# indexing dictionaries is a little different.
# you index a dictionary by its keys:
my_dict = {'riley': 'strange', 'keryn': 'super_cool'}
keryn_coolness = my_dict['keryn']

# you can also use these indices the other way -- to SET values instead of GET them.
# for example:
my_dict['riley'] = 'kinda cool'
my_list[0] = 999



# exercises:

# 1. strings are collections of characters -- they can be indexed too!
# try grabbing just the 'w' from my_string, and saving it to a new variable called my_w.
my_string = 'hello what is up my dude'
# your code here

# 2. select the 2 from my_list using a negative index and save the 2 to a new variable. 


# 3. remember how I said tuples are immutable? create a tuple and try changing one of its values using an index.  What happens? 