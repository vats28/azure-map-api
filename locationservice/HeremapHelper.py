import json
import requests

api_key = 'It1p0Cie4VSeGAhwOCXZluaM4755og543pFeZ2Wz2nE'

class HeremapHelper:
	def __init__(self,raw_coord):
		self.raw_coord = raw_coord

	def getDistances(self):
		coord_split = self.raw_coord.split(';')
		lat1 = coord_split[0].split(',')[0]
		long1 = coord_split[0].split(',')[1]
		lat2 = coord_split[1].split(',')[0]
		long2 = coord_split[1].split(',')[1]

		try:
			response1 = requests.get(f'https://route.ls.hereapi.com/routing/7.2/calculateroute.json?waypoint0={lat1}%2C{long1}&waypoint1={lat2}%2C{long2}&mode=shortest%3Bcar&traffic:enabled&apiKey={api_key}')
		except:
			response1 = requests.get(f'https://route.ls.hereapi.com/routing/7.2/calculateroute.json?waypoint0={lat1}%2C{long1}&waypoint1={lat2}%2C{long2}&mode=shortest%3Bcar&traffic:enabled&apiKey={api_key}')
		direction = response1.content.decode("UTF-8")
		direction = json.loads(direction)
		data = direction['response']['route'][0]['summary']

		source = lat1 + ',' + long1
		destination = lat2 + ',' + long2

		distance = str(data['distance']) + ' m'

		api_response = {
			'Source':f'{lat1},{long1}',
			'Destination':f'{lat2},{long2}',
			'Distance':f'{distance}'
		}

		return api_response


	def getNearByPlaces(self):

		coord_split = self.raw_coord.split(',')
		lat = coord_split[0]
		lon = coord_split[1]

		coordinates = lat + ',' + lon

		response1 = requests.get(f'https://reverse.geocoder.ls.hereapi.com/6.2/reversegeocode.json?prox={lat}%2C{lon}&mode=retrieveAddress&maxresults=1&apiKey={api_key}')


		response = requests.get(f'https://reverse.geocoder.ls.hereapi.com/6.2/reversegeocode.json?prox={lat}%2C{lon}&mode=retrieveLandmarks&maxresults=5&apiKey={api_key}')
		print(response1.content)

		response_data = response.content.decode("UTF-8")
		response_data = json.loads(response_data)

		response_data1 = response1.content.decode("UTF-8")
		response_data1 = json.loads(response_data1)

		suggestions = []
		address = response_data1['Response']['View'][0]['Result'][0]['Location']['Address']['Label']
		for d in response_data['Response']['View'][0]['Result']:
			place_name = d['Location']['Name']
			place_label = d['Location']['Address']['Label']
			nearby_place = f'{place_name},{place_label}'
			
			place_coord = d['Location']['DisplayPosition']
			s_lat = place_coord['Latitude']
			s_long = place_coord['Longitude']

			suggestion = {
					'Address':f'{nearby_place}',
					'Coordinates':f'{s_lat},{s_long}'
			}

			suggestions.append(suggestion)

		api_response = {
			'Coordinates':f'{lat},{lon}',
			'Address':f'{address}',
			'NearbyPlaces':f'{suggestions}',
		}


		return api_response
