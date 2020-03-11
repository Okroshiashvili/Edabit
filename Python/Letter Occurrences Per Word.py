


def find_occurrences(txt, ch):
    result = {}
    for i in txt.lower().split():
        result.update({i:i.count(ch.lower())})
    return result



# Test Case

print(find_occurrences("Hello World", "o")) # {
#   "hello" : 1,
#   "world" : 1
# }

print(find_occurrences("Create a nice JUICY function", "c")) #  {
#   "create" : 1,
#   "a" : 0,
#   "nice" : 1,
#   "juicy" : 1,
#   "function" : 1
# }

print(find_occurrences("An APPLE a day keeps an Archeologist AWAY...", "A")) # {
#   "an" : 1,
#   "apple" : 1,
#   "a" : 1,
#   "day" : 1,
#   "keeps" : 0,
#   "archeologist" : 1,
#   "away..." : 2
# }




