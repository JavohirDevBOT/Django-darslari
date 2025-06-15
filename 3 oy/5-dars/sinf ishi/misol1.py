class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __str__(self):
        return f"maxsulot: {self.name}"

    @property
    def total_price(self):
        return self.price * self.quantity



class Cart:
    def add_product(self, product:Product):
        return self.products.append(product)

    def remove_product(self, product:Product):
        return self.products.remove(product)

    def __init__(self):
        self.products:list[Product] = []

    def __bool__(self):
        return len(self.products) > 0

    def __len__(self):
        return len(self.products)

    def __contains__(self, key:str):
        for product in self.products:
            if product.name == key:
                return  True
        return False


    def __getitem__(self, key):
        return self.products[key]

    def __delitem__(self, key):
        del self.products[key]

    def __bool__(self):
        return bool(self.products)

    @property
    def total_sum(self):
        total_sum = 0
        for i in range(len(self.products)):
            total_sum += self.products[i].total_price
        return total_sum


# list, set, dict # ko'chirsa ikkalasi ham bitta narsa
# int, str, float, tuple # ko'chirsa ikkalasi har xil bo'ladi

# l = [10,3,50]
# l1 = l
# l1.append(100)
# print(l1)
# print(l1==l)
# print(l)
# a = 10
# b = a
# b = 30
# print(a,b)
#
# p1 = Product("Banan", 20000, 20)
# p2 = Product("Banan", 20000, 20)
# print(p1==p2)
# print(p1.total_price)
#
# cart = Cart()
#
#
# # print(len(cart))
# if cart: # is not None, list != [], int != 0
#     print("True")
# else:
#     print("False")

# p2 = p1
# print(p1 == p2)
p1 = Product("Monitor", 300, 1)
p2 = Product("Mouse", 50, 2)
l=[p1,p2]

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)
print(len(cart))         # 2
print(cart.total_sum)    # 400
print(cart[0])           # Monitor
print("Mouse" in cart)   # True
