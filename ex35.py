from sys import exit
def dead(why):
	print why, "Good job!"
	exit(0)
def gold_room():
	print "The room is full of gold , how much do you take?"
	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man learn to input a number!")
	print "how_much value is : ", how_much
	if how_much < 50:
		print "You are not greedy, you win!"
		exit(0)
	else:
		dead("You are too greedy, you are dead.")
gold_room()