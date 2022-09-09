class Student:
	student = 0

	def __init__(self, name, ta):
		self.name = name
		self.understanding = 0
		Student.student += 1
		print("There are now", Student.student, "students")
		ta.add_student(self)

	def visit_office_hours(self, staff):
		staff.assist(self)
		print("Thanks, " + staff.name)

class Professor:
	def __init__(self, name):
		self.name = name
		self.student = {}

	def add_student(self, student):
		self.student [student.name] = student

	def assist(self, student):
		student.understanding += 1



class MinList:
	"""A list that can only pop the small element"""
	def __init__(self):
		self.items = []
		self.size = 0

	def append(self, item):
		"""Appends an item to the MinList
		>>> m = MinList()
		>>> m.append(4)
		>>> m.append(2)
		>>> m.size
		2
		"""
		self.items.append(item)
		self.size +=1

	def pop(self):
		"""Removes and returns the smallest item from the MInList
		>>> m = MinList()
		>>> m.append(4)
		>>> m.append(1)
		>>> m.append(5)
		>>> m.pop()
		1
		>>> m.size
		2
		"""
		smallest = min(self.items)
		self.size -= 1
		self.items.remove(smallest)
		return smallest


class Email:
	"""Every email object has 3 instance attributes: the
	message, the sender name, and the recipient name.
	"""
	def __init__(self, msg, sender_name, recipient_name):
		self.msg = msg
		self.sender_name = sender
		self.recipient_name = recipient_name


class Server:
	"""Each Server has an instance attribute clients, which
	is a dictionary that associates client names with
	client objects.
	"""
	def __init__(self):
		self.clients = {}

	def send(self, email):
		"""Take an email and put it in the inbox of the client
		it is addressed to.
		"""
		client = self.clients[email.recipient_name] # 查找客户，由客户收取邮件
		client.receive(email)

		# email.recipient_name.recieve(email) # 不是查找客户名，而应该通过字典查找已注册客户

	def register_client(self, client, client_name):
		"""Takes a client object and client_name and adds them
		to the clients instance attribute.
		"""
		self.clients[client_name] = client



class Client:
	"""Every Client has instance attributes name (which is
	used for addressing emails to the client), server
	(which is used to send emails out to other clients), and
	inbox (a list of all emails the client has received).
	"""
	def __init__(self, server, name):
		self.inbox = []
		self.server = server
		self.name = name

	def compose(self, msg, recipient_name):
		"""Send an email with the given message msg to the
		given recipient client.
		"""
		email = Email(msg, self.name, recipient_name) # 创建邮件对象
		self.server.send(email) # 发送邮件

	def receive(self, email):
		"""Take an email and add it to the inbox of this
		client.
		"""
		self.inbox.append(email) # 收邮件


# class Dog():
# 	def __init__(self, name, owner):
# 		self.is_alive = True
# 		self.name = name
# 		self.owner = owner

# 	def eat(self, thing):
# 		print(self.name + " ate a " + str(thing) + "!")

# 	def talk(self):
# 		print(self.name + " says woof")

# class Cat():
# 	def __init__(self, name, owner, lives = 9):
# 		self.is_alive = True
# 		self.name = name
# 		self.owner = owner
# 		self.lives = lives

# 	def eat(self, thing):
# 		print(self.name + " ate a "+ str(thing) + "!")
# 	def talk(self):
# 		print(self.name + " says meow!")

class Pet():
	def __init__(self, name, owner):
		self.is_alive = True # It's alive!!!
		self.name = name
		self.owner = owner
	def eat(self, thing):
		print(self.name + " ate a " + str(thing) + "!")
	def talk(self):
		print(self.name)

class Dog(Pet):
	def talk(self):
		print(self.name + ' says woof!')

class Cat(Pet):
	def __init__(self, name ,owner, lives = 9):
		self.name = name
		self.owner = owner
		self.lives = lives

	def talk(self):
		"""Print out a cat's greeting

		>>> Cat('Thomas', 'Tammy').talk()
		Thomas says meow!
		"""
		print(self.name + " says meow!")

	def lose_life(self):
		"""Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
		becomes False. If this is called after lives has reached zero, print out
		that the cat has no more lives to lose.
		"""
		if self.lives > 0:
			self.lives -= 1
		else:
			print("the cat has no more lives to lose")

class NoisyCat(Cat): # Fill me in!
	"""A Cat that repeats things twice."""
	# def __init__(self, name, owner, lives=9):
		# Is this method necessary? Why or why not?
		# 不需要, 调用Cat的__init__即可.

	def talk(self):
		"""Talks twice as much as a regular cat.
		>>> NoisyCat('Magic', 'James').talk()
		Magic says meow!
		Magic says meow!
		"""
		print("{} says meow!\n{} says meow!".format(self.name, self.name))
	def __repr__(self):
		"""The interpreter-readable representation of a NoisyCat
		>>> muffin = NoisyCat('Muffin', 'Catherine')
		>>> repr(muffin)
		"NoisyCat('Muffin', 'Catherine')"
		>>> muffin
		NoisyCat('Muffin', 'Catherine')
		"""
		return "NoisyCat('{}', '{}')".format(self.name, self.owner)


