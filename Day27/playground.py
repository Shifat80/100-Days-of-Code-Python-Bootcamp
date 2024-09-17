# def add(*args):
# 	sum = 0
# 	for n in args:
# 		sum += n
# 	return sum
#
#
# print(add(4, 5, 6))

def calculator(n,**kwargs):
	n += kwargs["add"]
	n *= kwargs["multiply"]
	print(n)


calculator(2, add=3, multiply=5)
# class Car:
# 	def __init__(self,**kw):
# 		self.make = kw["make"]
# 		self.model= kw["model"]
# my_car = Car(make="Audi",model="R8")
#
# print(my_car.make)

class Car:
	def __init__(self,**kw):
		self.make = kw.get("make")
		self.model= kw.get("model")
		self.color = kw.get("Color")
my_car = Car(model="R8",color="White")

print(my_car.make)