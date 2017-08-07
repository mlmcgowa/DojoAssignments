# Making and Reading from Dictionaries

# Create a dictionary containing some information about yourself. The keys
# should include name, age, country of birth, favorite language.

def bio(x):
    for key in x:
        print "My", key, "is", x[key]


info = {"name":"Melinda", "age":"26", "country of birth":"United States", "favorite language":"Python",}

bio(info)
