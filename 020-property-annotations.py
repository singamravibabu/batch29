import random
class Die:
	def __init__(self):
		self.__value = 1

	# getter method
	@property
	def value(self):
		return self.__value

	# setter method
	@value.setter
	def value(self, value):
		if value < 1 or value > 6:
			raise ValueError("Value must be between 1 and 6.")
		else:
			self.__value = value