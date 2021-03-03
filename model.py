import json
import math 

class Agent :
# instantiation de classe avec un dictionnaire d'attributs pour chaque agent 
	def __init__(self,position, **agent_attributes):
		self.position=position
		for attribute_name, attribute_value in agent_attributes.items():
			setattr(self,attribute_name,attribute_value)

#coordinates of areas and agents 
class Position:
	def __init__(self, longitude_degrees,latitude_degrees):
		self.latitude_degrees= latitude_degrees
		self.longitude_degrees = longitude_degrees

#création des propriétés longitude et latitudes en radiant 
	@property
	def longitude(self):
		return self.longitude_degrees* math.pi /180
	@property
	def latitude(self): 
		return self.latitude_degrees* math.pi/180

class Zone: 
	MIN_LONGITUDE_DEGREES = -180
	MAX_LONGITUDE_DEGREES = 180
	MIN_LATITUDE_DEGREES = -90
	MAX_LATITUDE_DEGREES = 90
	WIDTH_DEGREES = 1 # degrees of longitude
	HEIGHT_DEGREES = 1 # degrees of longitude
	ZONES=[]
    
	def __init__(self, corner1, corner2):
		self.corner1 = corner1
		self.corner2 = corner2
		self.inhabitants = 0

	@classmethod
	def initialize_zones(cls):
		for latitude in range(cls.MIN_LATITUDE_DEGREES,cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
			for longitude in range(cls.MIN_LONGITUDE_DEGREES,cls.MAX_LONGITUDE_DEGREES,cls.WIDTH_DEGREES):
				bottom_left_corner = Position(longitude, latitude)
				top_right_corner = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
				zone = Zone(bottom_left_corner, top_right_corner)
				cls.ZONES.append(zone)
			print(len(cls.ZONES))
				#zone = bottom left corner & top right corner


#main function to load json file and extract agent_attributes then call Agent in order to create all the necessary Agent instances 
def main():
	Zone.initialize_zones()
	with open("agents-100k.json", "r", encoding="utf8") as contenu:
		data=json.load(contenu)
		for agent_attributes in data: 
			latitude = agent_attributes.pop('latitude')
			longitude= agent_attributes.pop('longitude')
			position=Position(latitude,longitude)
			agent=Agent(position, **agent_attributes)

main()


