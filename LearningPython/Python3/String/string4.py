import sys
print('-' * 80)
template = '{0}, {1} and {2}'					# By position
print(template.format('spam','ham','eggs'))
template = '{motto}, {pork} and {food}'			# By keyword
print(template.format(motto='spam', pork='ham',food='eggs'))
template = '{motto}, {0} and {food}'			# By both
print(template.format('ham', motto='spam', food='eggs'))
template = '{}, {} and {}'						# By relative position (New in 3.1 and 2.7)
print(template.format('spam','ham','eggs'))
print('%s, %s and %s' % ('spam','ham','eggs'))
template = '%(motto)s, %(pork)s and %(food)s'
print(template % dict(motto='spam',pork='ham',food='eggs'))
x = '{motto}, {0} and {food}'.format(42, motto=3.14,food=[1,2])
print(x)
print(x.split(' and '))
y = x.replace('and', 'but under no circumsances')
print(y)
print('My {1[kind]} runs {0.platform}'.format(sys, {'kind':'laptop'}))
print('My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind':'laptop'}))
somelist = list('SPAM')
print(somelist)
print('first={0[0]}, third={0[2]}'.format(somelist))
print('first={0}, last={1}'.format(somelist[0], somelist[-1]))
parts = somelist[0], somelist[-1], somelist[1:3]
print('first={0}, last={1}, middle={2}'.format(*parts))
s = 'IamHarryCheng'
i = s.find('Harry')
print(s[1:i])
print('-' * 80)