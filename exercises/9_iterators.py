# an ITERABLE object in python is one that contains other objects -- so a list, a dict, a tuple, a string, etc. 

# iterators are a powerful way to perform sequential or repetitive operations on your data.
# especially useful in biology, data cleaning, etc!

# python has two built-in ways to iterate: for, while

# let's start with while
# it works by repeating infinitely while a given condition is true

#   while condition:
#       cool_function()
#       fixing_my_data()

# obviously, you don't want your program to repeat infinitely. Usually, you create a variable and modify it on each loop
# such that the condition will eventually be false

max_loops = 100
x = 0
my_cool_list = []

while x <= max_loops:
    my_cool_list.append('howdy')
    x += 1

# print out my_cool_list to check it out!


### Next, let's look at for loops. 

# For loops run over a finite set of items. 

# Take a look at the syntax:

for i in [0,1,2,3,4,5]:
    print(i)

# Think of this like: for each element 'i' in the list [0..5], print(i).
# This code will loop 6 times, and each time through, i will represent the next value in the iterable object (the list [0..5])

# Keep the biological applications in mind here: this is an incredibly powerful tool!
# not only can it speed up your tasks, it can open doors to research you wouldn't have otherwise been able to complete at all!
# i.e.
    # for genome in list_of_genomes:
        # remove_bad_reads(genome)
        # compute_similarity_scores(my_phylo, genome)
        # bootstrap_it(my_phylo, genome)
        # place_in_phylogeny(my_phylo, genome)

    # for tree in rileys_field_sites:
        # simulate_local_climate(tree.get_environment())
        # calculate_hydraulic_failure_prob(tree.get_hydraulics())


# exercises:

# 1. Write a while loop that DOESN'T run infinitely. Can be a total ripoff of the one above.

# 2. Write a while loop that runs infinitely. Just for funsies. Run it. Then use ctrl + C to kill the process. (not command! it's control!)

# 3. Use a for loop to find the average of this list: 
cool_list = [1,2,5,8888,6,4,8]
# note that there are easy built-in methods to do stuff like averages on lists
# irl, you should use the built-in methods
# but this is just practice writing a for loop


# 4. (Challenge) use two loops to print every possible pairwise combination of names in these two lists.
# your output should be:
# NicoRiley
# NicoAliya
# NicoCaitlin
# DamienRiley
# DamienAliya
# DamienCaitlin
# John LillRiley
# John LillAliya
# John LillCaitlin

cool_dudes = ['Nico', 'Damien', 'John Lill']
weird_dudes = ['Riley', 'Aliya', 'Caitlin']