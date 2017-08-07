# Stars
# Write the following functions.

# Part I
# Create a function called draw_stars() that takes a list of numbers and prints
# out *.

# def draw_stars(arr):
#     for i in arr:
#         print ('*' * i)
#
# draw_stars([4, 6, 1, 3, 5, 7, 25])

# Part II
# Modify the function above. Allow a list containing integers and strings to be
# passed to the draw_stars() function. When a string is passed, instead of
# displaying *, display the first letter of the string according to the example
# below. You may use the .lower() string method for this part.

def draw_stars(arr):
    for i in arr:
        if type(i) == int:
             print ('*' * i)
        elif type(i) == str:
            print (i[0] * len(i))

draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
