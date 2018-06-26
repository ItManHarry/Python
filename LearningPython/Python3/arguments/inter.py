def intersect(*args):
	res = []
	for x in args[0]:
		if x in res:
			continue
		for other in args[1:]:
			if x not in other:
				break
		else:
			res.append(x)
	return res
def intersect2(*args):
	result = []	
	for x in args[0]:
		if x in result:
			continue
		else:
			b = True
			for others in args[1:]:
				if x not in others:
					b = False
					break
			if b:
				result.append(x)
	return result					
print(intersect(intersect('SPAM', 'SCAM'),'CAM'))
print(intersect('SPAM','SCAM','SPAM'))
print(intersect2('SPAM','SCAM','SPAM'))