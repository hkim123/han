def get_gender(sex = "unknown"):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex)

get_gender('m')
get_gender('f')
get_gender() # this case no input, so the value will be default value "unknown" but if I put any other value, it print out that value
             # so below program is any other value will be print out unknown
get_gender('k') # this case it print out 'k'


def get_gender(sex = "unknown"):
    if sex is 'm':
        sex = "Male"

    elif sex is 'f':
        sex = "Female"

    else:
        sex = "unknown"

    print(sex)

get_gender('m')
get_gender('f')
get_gender()
get_gender('k')


# keyword argument

def dump_sentense (name = "bucky", action= "ate", item="tuna"):
    print (name,action,item)

dump_sentense()
dump_sentense("Sally","farts", "gently") # Sally is name and fart is action and gently is item
dump_sentense(item='awesome', action='is') # name is default value choose bucky but others are change to another value like "awesome" and "is"


### Unpacking Argument ####

def health_calculator (age, apple_ate, cigs_smoked):
    answer = (100-age)+(apple_ate * 3.5) - (cigs_smoked *2)
    print (answer)

person_1_data = [27, 20, 0]
health_calculator(person_1_data[0], person_1_data[1], person_1_data[2])
health_calculator(*person_1_data)  ## this is same as above we can save a lot of line