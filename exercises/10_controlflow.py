# let's keep working on conditional logic!

# now that we know how to write statements that evaluate to True or False, we can use them in if/else statements. 

if 5 > 7:
    print("howdy")
else:
    print("not howdy")


# if you have multiple conditions to check, you can add an "elif", short for "else if"

if 'z' in 'riley':
    print('impossible to reach this')
elif 'z' in 'zambia':
    print('wow nice we made it here')
else:
    print('in my mind palace, i am retired')


# exercises:

# 1. Write an if/else statement that works.  Feel free to mostly copy mine. Pay careful attention to the indents & formatting!

# 2. Write a function to check if the letter k is in a name.  It should return True or False. Here's the first part for you:

def my_function(name):
    # your code here!

# run this block of code to check if your function works!
test1 = my_function('riley')
test2 = my_function('keryn')
if not test1 and test2: 
    print('success!')
else:
    print('try again dawg')


# 3. Write a for loop that appends only numbers > 10 to the cool_list. 

cool_list = [] # cool list starts empty
input_list = [1,2,6,787,333,63,1,87,3]
for i in input_list:
    # your code here