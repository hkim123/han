def add_number(*args): # means can put many argument here
    total = 0
    for a in args:
        total += a # this is same as keep add. if args is one value total is that value but if args is 2 value like 3,34
                   # first 3 is in total so 3 + second a(34) it print out 37
                # total += 1 means total + 1
    print (total)

add_number(3)
add_number(3,34)
add_number(4,45,1245)

### if change from += to =+
def add_number(*args): # means can put many argument here
    total = 0
    for a in args:
        total =+ a # if i change to =+ it only print out last one (3,34,1245) this is same as total = a

    print (total)

add_number(3)
add_number(3,34)
add_number(4,45,1245)



##### if print is not correct position the result is different

def add_number(*args): # means can put many argument here
    total = 0
    for a in args:
        total += a
        print (total)

add_number(3)
add_number(3,34)
add_number(4,45,1245)