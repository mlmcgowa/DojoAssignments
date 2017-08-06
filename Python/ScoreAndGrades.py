# Assignment: Scores and Grades

# Write a function that generates ten scores between 60 and 100. Each time a
# score is generated, your function should display what the grade is for a
# particular score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

import random

def grade():
    for num in range(0,10):
        score = random.randint(60,100)

        if score >= 90:
            print "Score:", score, "Grade: A"
        elif score >= 80:
            print "Score:", score, "Grade: B"
        elif score >= 70:
            print "Score:", score, "Grade: C"
        elif score >= 60:
            print "Score:", score, "Grade: D"

grade()
