def my_decorator(func):
	def name():
		print("Before")
		func()
		print("After")
	return name

@my_decorator
def some():
	print("some function")

some()