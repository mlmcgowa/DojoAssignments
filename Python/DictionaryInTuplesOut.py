def tuple(dict):
    list = []
    for key in dict:
        tup = (key, dict[key])
        list.append(tup)
    return list

dict = {
"Speros": "(555) 555-5555",
"Michael": "(999) 999-9999",
"Jay": "(777) 777-7777"
}
x = tuple(dict)
print x
