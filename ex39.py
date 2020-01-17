states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}

cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '--' * 25
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print '--' * 25
print "Michigan's abbrevation is: ", states['Michigan']
print "Florida's abbrevation is: ", states['Florida']

print '--' * 25
for state, abbrev in states.items():
    print "%s is abbrevated %s " % (state, abbrev)
    
print '--' * 25
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

print '--' * 25
for state, abbrev in states.items():
    print "%s state is abbrevated %s and has city %s" % (state, abbrev, cities[abbrev])

print '--' * 25
state = states.get('Texas', None)

if not state:
    print "Sorry, No texas."

city = cities.get('TX', 'DNE')
print "The city for the state 'TX' is: %s" % city	
	