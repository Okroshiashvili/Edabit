

def how_many_times(num):
    return "Ed{}bit".format(num * 'a')



# Test case

print(how_many_times(5)) # "Edaaaaabit"

print(how_many_times(0)) # "Edbit"

print(how_many_times(12)) # "Edaaaaaaaaaaaabit"


