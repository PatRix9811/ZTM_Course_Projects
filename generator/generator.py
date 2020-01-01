class MyGen():
	start = 0

	def __init__(self,*args,**kwargs):
		count = len(args)
		if count == 3:
			MyGen.start = args[0]
			self.stop = args[1]
			self.step = args[2]
		elif count == 2:
			MyGen.start = args[0]
			self.stop = args[1]
			self.step = 1
		elif count == 1:
			self.stop = args[0]
			self.step = 1


	def __next__(self):
		if MyGen.start > self.stop:
			raise StopIteration

		num = MyGen.start
		MyGen.start += self.step
		return num

	def __iter__(self):
		return self


for i in MyGen(100):
	print(i)