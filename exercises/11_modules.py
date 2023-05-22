# python has a great modular import system that allows you to leverage external libraries and scripts in your code.

# you can import code using these keywords:

# import x
# import x as y 
# from x import z

# python ships with a few useful modules for import. here's an example.

import math

math.sqrt(100)

# typically, your imports go at the top of your script. 
# it's generally good practice to import only the functions that you need. 
# for example, if you're only going to use the sqrt() function from the math module, 
# this might be preferable to the above code:

# from math import sqrt
# sqrt(100)

# if libraries have verbose names, or if you use them frequently, it can be advantageous to abbreviate the name:

import numpy as np
import pandas as pd
x = np.array([1,2,3])

# numpy and pandas are external libraries.  They do not come stock with python. 
# They are pretty popular, however. Github has pre-installed them into our codespace for us, apparently. 

# external libraries are typically installed on the command line with:
# pip install packagename

# though if you're using a package manager like poetry or conda, it might be:
# poetry add packagename
# conda install packagename
# etc

# finally, you can import modules from your own local projects!
# check this out:

from exercises.my_example_module import cool_external_function as cef

cef()

