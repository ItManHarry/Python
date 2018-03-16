# _*_ coding:utf-8 _*_
__author__ = 'Harry'
class Lexicon(object):
	def __init__(self):
		self.directions = ('south','north','west','east','center')
		self.verbs = ('go','kill','eat','run','tell','shoot','sing','love')
		self.stops = ('the','in','of','to','via')
		self.nouns = ('bear','princess','MissHei','tiger','dragon')
		self.sen = []
	def scan(self, sentence):
		self.sentence = sentence
		words = self.sentence.split(' ')
		print "The words is : ",words
		self.sen = []
		for word in words:
			if word in self.directions:
				self.sen.append(('direction', word))
			elif word in self.verbs:
				self.sen.append(('verb', word))
			elif word in self.stops:
				self.sen.append(('stop', word))
			elif word in self.nouns:
				self.sen.append(('noun', word))
			else:					
				self.sen.append(('number', self.convert_number(word)))
		return self.sen
	def convert_number(self, s):
		try:
			return int(s)
		except ValueError:
			return s
lexicon = Lexicon()
lexicon.scan("north")
print lexicon.sen
lexicon.scan('in the south there is a gold house I want to go maybe there should be a bear on the road or a dragon 34 90')
for tuple in lexicon.sen:
	print "Tuple is : ", tuple