class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line			
class MyStuff():
	def __init__(self):
		self.age = 35
		self.name = "Harry"
		self.birthday = "1983-11-02"
	def apple(self):
		print "I am MyStuff's Apple."
	def info(self):
		print "My information is : {Name : %s, Age : %d, Birthday : % s}" %(self.name, self.age, self.birthday)
	address = ""
print "-" * 80
happy_birth = Song(["Happy birthday to you",
    "happy birthday to you ",
	"happy birthday to my friend"])
happy_birth.sing_me_a_song()
print "-" * 80
bulls_on_parade = Song(["ABCDEFG",
	"HIJKLMN",
	"OPQRST",
	"UVWXYZ",
	"XYZ, NOW YOU SEE", 
	"I CAN SAY MY ABC"])
bulls_on_parade.sing_me_a_song()
print "-" * 80
print happy_birth.lyrics
my_stuff = MyStuff()
print "-" * 80
print my_stuff.age
my_stuff.apple()
my_stuff.info()
my_stuff.address = "YT CHINA"
print my_stuff.address