

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age    
  
    def compare_age(self, other):
        if self.age > other.age:
            return ("{} is younger than me.".format(other.name))
        elif self.age < other.age:
            return ("{} is older than me.".format(other.name))
        else:
            return ("{} is the same age as me.".format(other.name))





# Test Case

p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)


print(p1.compare_age(p2)) # "Joel is older than me."
print(p2.compare_age(p1)) # "Samuel is younger than me."
print(p1.compare_age(p3)) # "Lily is the same age as me."




