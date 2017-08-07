# Coin Tosses

# Write a function that simulates tossing a coin 5,000 times. Your function
# should print how many times the head/tail appears.

import random
import decimal

def coin_toss(num):

    heads = 0
    tails = 0

    for i in range(0,num):
        toss = (random.randint(0,101))
        print toss
        # create_decimal = (divide(toss,100))
        # divide(toss,100)

    if toss <= 49:
        heads += 1
        print "Toss #", i, "You now have tossed", heads, "head(s) and", tails, "tail(s) so far"

    elif toss >=50:
        tails += 1
        print "Toss #", i, "You now have tossed", heads, "head(s) and", tails, "tail(s) so far"

coin_toss(11)
