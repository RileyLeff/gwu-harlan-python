# programs often rely heavily on conditional logic.
# For example:
    # do A if B, else, do C. 

# To implement this, you'll need to use expressions that check whether a condition is True or False. 
# In python, here's a few of our options:

## COMPARISON
1 == 1 # double equals signs check for equality, true if equal, false if not
1 != 1 # this checks for INEQUALITY, returning true if they're NOT equal
1 > 2 # these work as you might expect
1 >= 2
1 < 2
1 <= 2

## LOGICAL
True and True
True and False
False and False
True or False
True or True
False or False
not 1 < 2
not 1 > 2

## Identity
True is True # what's the difference between "is" and "=="?
True is not False

## Membership
5 in [1,2,3,4,5]
9 not in [1,2,3]

### EXERCISES

# What will these print out?

# 1.  
not not 5 == 5

# 2.
1 == 2 or 3 in ['1', '2', '3']
 
# 3. 
x = [1,2,3]
y = [1,2,3,4]
z = y
x.append(4)
z == y
z is y
x == y 
x is y
