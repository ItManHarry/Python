print "-" * 100
stuff = {"name":"Harry","Age":35,"Sex":"M"}
print stuff["name"]
stuff["company"] = "Doosan"
print stuff
stuff["home"] = "YT Gold Garden"
print stuff["home"]
print stuff
print "-" * 100
states = {
	'Oregon':'OR',
	'Florida':'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI'
}
cities = {
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonville'
}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
print states
print "-" * 100
print "NY state has : ", cities['NY']
print "OR state has : ", cities['OR']
print "-" * 100
print "Michigan's abbreviation is : ", states['Michigan']
print "Florida's abbreviation is : ", states['Florida']
print "-" * 100
print "Michigan has : ", cities[states['Michigan']]
print "Florida has : ", cities[states['Florida']]
print "-" * 100
for state, abbrev in states.items() : 
	print "%s's abbreviation is %s" %(state, abbrev)
print "-" * 100
for abbrev, city in cities.items() :
	print "%s's the city %s" % (abbrev, city)
print "-" * 100
for state, abbrev in states.items() :
	print "%s state is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev])
print "-" * 100
state = states.get('Texas', None)
if not state :
	print "Sorry, no Texas."
print "-" * 100
city = cities.get('TX', 'Does not exist')
print cities
print "City TX : %s" % city
print "-" * 100
cities['TX'] = "Safacisco"
print cities
print "-" * 100