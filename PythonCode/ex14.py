# _*_ coding:utf-8 _*_
from sys import argv
script, user_name, user_age = argv
prompt = ">"

print "Hi %s, I'm %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have %s?" % user_name
computer = raw_input(prompt)

print """
	Alright, %s (%r years old):
	You said %r about like me.
	You like in %r. NOt sure where that is.
	And you have a %r computer. Nice
""" % (user_name, user_age, likes, lives, computer)