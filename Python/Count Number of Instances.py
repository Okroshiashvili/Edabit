

class User:

	user_count = 0

	def __init__(self, name):
		self.username = name
		User.user_count += 1



# Test Cases

u1 = User("johnsmith10")
print(User.user_count) # 1

u2 = User("marysue1989")
print(User.user_count) # 2

u3 = User("milan_rodrick")
print(User.user_count) # 3


print(u1.username) # "johnsmith10"

print(u2.username) # "marysue1989"

print(u3.username) # "milan_rodrick"
