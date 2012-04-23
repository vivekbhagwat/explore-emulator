import urllib2
import json
import secret

# response = urllib2.urlopen('https://foursquare.com/oauth2/authenticate?client_id=' + secret.client_id )

# print response.read()

lat = raw_input('What is your latitude? (e.g. 40.799921) ')
lng = raw_input('What is your longitude? (e.g. -73.96831) ')
lat = str(float(lat)) if lat != '' else '40.799921'
lng = str(float(lng)) if lng is not '' else '-73.96831'

query = raw_input('Would you like to look for something in particular? (if not just press enter) ')

print 'Getting ' + ((query + '-related ') if query else '') + 'venues near ' + lat + ', ' + lng + '...'



url = 'https://api.foursquare.com/v2/venues/search'
url += '?ll='+lat+','+lng
url += '&query='+query if query else ''
url += '&limit=50'
url += '&oauth_token='+secret.oauth_token+'&v=20120422'
print url
response = urllib2.urlopen(url)
html = response.read()

venues = json.loads(html)[u'response'][u'venues']
print venues
print len(venues)

hereNow = venues[5][u'hereNow'][u'count']
totalCheckins = venues[5][u'stats'][u'checkinsCount']

print hereNow
print totalCheckins

# print html
