

def add_ending(lst, ending):
    return [i + ending for i in lst]





# Test case

print(add_ending(["clever", "meek", "hurried", "nice"], "ly")) # ["cleverly", "meekly", "hurriedly", "nicely"]

print(add_ending(["new", "pander", "scoop"], "er")) # ["newer", "panderer", "scooper"]

print(add_ending(["bend", "sharpen", "mean"], "ing")) # ["bending", "sharpening", "meaning"]



