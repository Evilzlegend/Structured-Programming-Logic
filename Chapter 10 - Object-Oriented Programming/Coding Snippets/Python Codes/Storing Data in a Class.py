# Topic Summary:

# Objects are meant to store date as well as methods, and to use methods to access and manipulate the
# data. Data for a class is given as instance variables, variables that belong to the objects of the class.
# They may be created anywhere in a class as needed. They are sometimes created outside of any
# method, as a statement in the class declaration. When created or used inside a method, they are
# tagged with the label self to distinguish them from regular local variables of the method.

# Playing with Coding Snippets:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

class Rodent:
	# instance variables declared outside method:
	hasFur = True
	myName = ""

	def bite(self, num=1):
		for i in range(num):
			print("Bite!")

	def chew(self, num=1):
		for i in range(num):
			print("Chew!")

	def setName(self, name):
		self.myName = name # updating instance variable

	def getName(self):
		return "Rodent " + self.myName # using instance variable

rat = Rodent()
rat.bite(3)
rat.chew()
print(rat.getName())
rat.setName("Justin")
print(rat.getName())