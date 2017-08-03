# Write a program that takes a list and prints a message for each element
# in the list, based on that element's data type.

# For each item in the list, test its data type. If the item is a string,
# concatenate it onto a new string. If it is a number, add it to a running sum.
# At the end of your program print the string, the number and an analysis of
# what the list contains. If it contains only one type, print that type,
# otherwise, print 'mixed'.

def typelist(x):

    sum = 0
    string = ''

    # if (isinstance(i, int) for i in x):
    #     print "The list you entered is of mixed type.""

    if (isinstance(i, int) or isinstance(i, float) for i in x):
        print "The list you entered is of integer type."

    elif (isinstance(i, str) for i in x):
        print "The list you entered is of string type."

    for i in x:

        if type(i) is int:
            sum += i
            print 'Sum:' + str(sum)

        if type(i) is str:
            string += ',' + i
            print string

# print string
# print 'Sum:' + str(sum)

typelist(['magical unicorns',19,21,'hello',98.98,'world'])
