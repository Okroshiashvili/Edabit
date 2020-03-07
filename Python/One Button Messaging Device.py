


def how_many_times(msg):
    if msg == "":
        return 0
    else:
        return ord(msg[0]) - 96 + how_many_times(msg[1::])




# Test case

print(how_many_times("abde")) # 12

print(how_many_times("azy")) # 52

print(how_many_times("qudusayo")) # 123


