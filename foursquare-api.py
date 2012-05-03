import urllib2
import json
import secret
import time
import numpy as np

class Foursquare:
	"""docstring for Foursquare"""
	def __init__(self):
		# super(Foursquare, self).__init__()
		self.feature_vector = np.array([0])
        self.feature_weights = np.array([1.0])
        self.feature_dict = {'popular' : 0}
        self.oauth_token = secret.oauth_token

        self.lat, self.lng = self.get_location()
		
    def get_location(self):
	    lat = raw_input('What is your latitude? (e.g. 40.799921) ')
		lng = raw_input('What is your longitude? (e.g. -73.96831) ')
		lat = str(float(lat)) if lat != '' else '40.799921'
        lng = str(float(lng)) if lng is not '' else '-73.96831'

        return lat, lng

	def get_venues_nearby():
		#query = raw_input('Would you like to look for something in particular? (if not just press enter) ')

		# print 'Getting ' + ((query + '-related ') if query else '') + 'venues near ' + lat + ', ' + lng + '...'

		url = 'https://api.foursquare.com/v2/venues/search'
		url += '?ll='+self.lat+','+self.lng
		#url += '&query='+query if query else ''
		url += '&limit=50'
		url += '&oauth_token='+self.oauth_token+'&v=20120422'
		# print url
		response = urllib2.urlopen(url)
		html = response.read()

		venues = json.loads(html)[u'response'][u'venues']
		# print venues
		# print len(venues)

		# hereNow = venues[5][u'hereNow'][u'count']
		# totalCheckins = venues[5][u'stats'][u'checkinsCount']
		# categories = venues[5][u'categories']

		# all_categories = []
		# for v in venues:
			# all_categories.append(len(v[u'categories']))


		# print hereNow
		# print totalCheckins
		# print categories
		# print all_categories

		return venues


    #train
	def get_checkin_history(self):
		venues_list = []
		offset = 0
		count = 0

		while True:
			url = 'https://api.foursquare.com/v2/users/self/checkins'
			url += '?oauth_token='+self.oauth_token+'&v='+time.strftime("%Y%m%d")
			url += '&offset='+str(offset)+'&limit=100'

			print url

			response = urllib2.urlopen(url)
			html = response.read()

			json_response = json.loads(html)['response']
			count = json_response['checkins']['count']
			# print 'count = ', count

			venues = json_response['checkins']['items']
			# print venues
			# print len(venues)

			venues_list.extend(venues)

			offset += len(venues)

			if offset >= count:
				break
		return venues_list

    #returns index in weights/vector, augments weight
	def add_to_feature_vector(self, category_key):
       
       if category_key not in self.feature_dict:
           self.feature_dict[category_key] = len(self.feature_vector)
           self.feature_vector.append(1)
           self.feature_weights.append(0.0)
           
       self.feature_weights[self.feature_dict[category_key]] += 1.0 

       return self.feature_dict[category_key]
        
		


fq = Foursquare()

history = fq.get_checkin_history()
for v in history:
    popular = False
    category = v['categories']['shortName']
    print fq.add_to_feature_vector(category)


# print html







