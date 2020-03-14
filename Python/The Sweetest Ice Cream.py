


class IceCream:

    def __init__(self, flavor, num_sprinkles):
        self.flavor = flavor
        self.num_sprinkles = num_sprinkles


def sweetest_icecream(lst):
    my_dict = {"Plain":0, "Vanilla":5,
                "ChocolateChip":5, "Strawberry":10,
                "Chocolate":10}
    return max([my_dict.get(i.flavor,0) + i.num_sprinkles for i in lst])

        

### Flavors Table ###

# Plain	0
# Vanilla	5
# ChocolateChip	5
# Strawberry	10
# Chocolate	10


# Test case

ice1 = IceCream("Chocolate", 13)         # value of 23
ice2 = IceCream("Vanillla", 0)           # value of 5
ice3 = IceCream("Strawberry", 7)         # value of 17
ice4 = IceCream("Plain", 18)             # value of 18
ice5 = IceCream("ChocolateChip", 3)      # value of 8


print(sweetest_icecream([ice1, ice2, ice3, ice4, ice5])) # 23

print(sweetest_icecream([ice3, ice1])) # 23

print(sweetest_icecream([ice3, ice5])) # 17



