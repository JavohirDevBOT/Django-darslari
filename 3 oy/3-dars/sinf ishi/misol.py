class User:
    def __init__(self, username,familya):
        self.username = username
        self.familya = familya

    def __eq__(self, other):
        return self.familya == other.familya

# u1 = User("ali")
# u2 = User("ali")
f1= User("ziyodull")
f2= User("ziyodull")
print(f2 == f1)
print(u1 == u2)  # True
