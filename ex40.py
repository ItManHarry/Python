class Song(object):
	def __init__(this, lyrics):
		this.lyrics = lyrics
	def sing_me_a_song(this):
		for line in this.lyrics:
			print line
class MyStuff():
	def __init__(this):
		this.age = 35
		this.name = "Harry"
		this.birthday = "1983-11-02"
	def apple(this):
		print "I am MyStuff's Apple."
	def info(this):
		print "My information is : {Name : %s, Age : %d, Birthday : % s}" %(this.name, this.age, this.birthday)
happy_birth = Song(["Happy birthday to you",
	"happy birthday to you ",
	"happy birthday to my friend"])
happy_birth.sing_me_a_song()
print happy_birth.lyrics
my_stuff = MyStuff()
print my_stuff.age
my_stuff.apple()
my_stuff.info()