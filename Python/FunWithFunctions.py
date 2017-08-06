# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop
# executes have your program print the number of that iteration and specify
# whether it's an odd or even number.

# def odd_even():
#     for num in range(1,2001):
#         if num % 2 == 0:
#             print num, "is an even number"
#         else:
#             print num, "is an odd number"
#
# odd_even()

# Multiply:
# Create a function called 'multiply' that iterates through each value in a
# list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been
# multiplied by 5.

def multiply(list,num):
    for i in range(len(list)):
        list[i] *= num

    print list

# multiply([2,3,4],5)

def layered_multiples(arr):
    new_array = []
    for i in arr:
        new_array.append(['1' * i])
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
