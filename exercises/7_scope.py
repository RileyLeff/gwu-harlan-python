# Exercises:

# 1. Can you modify a global variable (i.e. one that lives outside of a function) from inside of a function?
    # Try it out!


# 2. In your opinion, would it be good practice or bad practice to modify a global variable from inside of a function? 
#   would this make it easier or harder to troubleshoot problems with your program?

x = 5
def hi(a, b, c):
    x = 6
    return(a + b + c)

print(x)
hi(1,2,3)
print(x)