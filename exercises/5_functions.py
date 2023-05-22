# functions are essentially chunks of code that can be used over and over again.

# imagine you have a task that you want to do a bunch of times.
# i.e. given a bunch of lists, you want to take out the first and last elements, and average them. 

list1 = [0,12,2,4,5,6,7,87,4]
list2 = [1,2,6,78,5,4,67,9]
list3 = [6,3,233,7,87,9]

# BAD PRACTICE BUT UNFORTUNATELY VERY COMMON IN BIOLOGY!
list1avg = (list1[0] + list1[-1]) / 2
list2avg = (list2[0] + list2[-1]) / 2
list3avg = (list3[0] + list3[-1]) / 2

# see how repetitive this is?
# if you copied down the same few lines of code for each list, it would take a really long time!
# might as well use excel at that point!

# good programmers write functions to avoid repeating themselves unnecessarily.

# in python, you generally use functions like this:
# name_of_function(argument1, argument2, argumentN, etc)

# you can define (note that def comes from --> define) custom functions like this:

def my_cool_function(argument):
    output = (argument[0] + argument[-1]) / 2 
    return(output)

# that would improve the above code considerably!
# instead of writing the same process over and over, we could use our function:

list1avg = my_cool_function(list1)
list2avg = my_cool_function(list2)
list3avg = my_cool_function(list3)

# while this is better, note that we're still repeating ourselves! we'll learn how to improve this further in section 8 (iterators). 
# for now, let's focus on functions for a bit. 

# IMPORTANT Note:
# pay attention to the indentation in the function above!  in python, INDENTATION IS PART OF THE SYNTAX!
# we'll talk about this more in the control flow section. 


# Exercises
# 1. following the format of the custom function provided above, 
# write a function that accepts one argument, adds 5 to the argument, prints the word "howdy", then returns the argument incremented by 5
# try it out in your interpreter!  Since the function will occupy multiple lines, you'll need to highlight the whole function before running it, 
# so that the interpreter knows to keep reading on. 



# 2. python comes with a lot of very useful functions built-in.
# we've already seen a few:
#   print()
#   type()
#   str()

# here's a few more!
# everyone should pick one of these, and google it.
# take a crack at explaining what it does, what it takes as its inputs, and what it outputs.
# if it has default behavior, let us know what they are!
# would love a quick demo of each if we have time

# riley will demo this one:
# all()

# len()
# round()
# filter()
# zip()
# reversed()
# bin()


