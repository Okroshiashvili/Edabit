


class Name:
    def __init__(self, fname, lname):
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        self.fullname = ' '.join([self.fname, self.lname])
        self.initials = self.fname[0] + '.' + self.lname[0]


# Test case

a = Name('john', 'SMITH')

print(a.fname)

print(a.lname)

print(a.fullname)

print(a.initials)


