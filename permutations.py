# Author: Nguyen L.
# Date: May 3rd
# Write a program to find permutations of a list of integers

# import a method
from itertools import permutations

# defining a function
def findPermutations(combo):

    # use the permutations method
    my_list = permutations(combo)

    for i in my_list:
        print(i)

my_list = input("Enter a list of numbers separated by a space: ")
my_list = my_list.split()

# convert all to intengers
for i in range(0, len(my_list)):
    my_list[i] = int(my_list[i])

# calling on the function findPermutations
findPermutations(my_list)