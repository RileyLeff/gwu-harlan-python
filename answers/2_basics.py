# 1 can you overwrite a variable?

x = 10
x = 11

if x == 11:
    print("1. yes, you can overwrite a variable!")
elif x == 10:
    print("1. no, you can't overwrite a variable!")
else:
    print("1. man something weird and wrong happened here.")


# 2 are names case sensitive?

foo = "bar"
FOO = "cool"

if foo == FOO:
    print("2. names are not case-sensitive")
else:
    print("2. names are case-sensitive!")
