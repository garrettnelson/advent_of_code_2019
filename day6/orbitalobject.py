class DistancePlanetMap(object):
	def __init__(self,orbit,distance):
		self.orbit = orbit
		self.distance = distance
class OrbitalObject(object):
	def __init__(self,name):
		self.orbits = []
		self.name = name
	def add_Orbit(self,orbitalObject):
		self.orbits.append(orbitalObject)
	def __repr__(self):
		orbits_string = ""
		for orbit in self.orbits:
			orbits_string += "%s," % orbit.name
		return "Orbit %s, orbits %s" % (self.name,orbits_string)
	def number_of_orbits(self):
		return len(self.orbits)
	def all_orbits(self):
		sub_orbits = 0
		for orbit in self.orbits:
			sub_orbits += orbit.all_orbits()
		return sub_orbits + self.number_of_orbits()
	def get_orbit_maps(self,initial_distance=0):
		maps = []
		for orbit in self.orbits:
			maps.append(DistancePlanetMap(orbit,initial_distance+1))
			for orbit_map in orbit.get_orbit_maps(initial_distance+1):
				maps.append(orbit_map)
		return maps
class ObjectMap(object):
	def __init__(self,from_file=None,from_text=None,debug=False):
		self.orbit_directory = {}
		self.debug = debug
		if from_file != None:
			self.load_from_file(from_file)
		if from_text != None:
			self.load_text(from_text)
	def load_from_file(self,from_file):
		f = open(from_file)
		text = f.read()
		f.close()
		self.load_text(text)
	def load_text(self,from_text):
		orbit_texts = from_text.split("\n")
		for orbit in orbit_texts:
			splitter = orbit.split(")")
			left = splitter[0]
			right = splitter[1]
			if not left in self.orbit_directory:
				self.orbit_directory[left] = OrbitalObject(left)
			if not right in self.orbit_directory:
				self.orbit_directory[right] = OrbitalObject(right)
			left_object = self.orbit_directory[left]
			right_object = self.orbit_directory[right]
			if self.debug:
				print "Adding %s as orbiting %s" % (right_object,left_object)
			right_object.add_Orbit(left_object)
	def calculate_check_sum(self):
		checksum = 0
		for key in self.orbit_directory:
			checksum += self.orbit_directory[key].all_orbits()
		return checksum
	def distance_from_you_to_san(self):
		san = self.orbit_directory["SAN"]
		you = self.orbit_directory["YOU"]
		distance_maps_for_san = san.get_orbit_maps()
		distance_maps_for_you = you.get_orbit_maps()

		combine = {}
		for map_distance in distance_maps_for_you:
			if not map_distance.orbit.name in combine:
				combine[map_distance.orbit.name] = []
			combine[map_distance.orbit.name].append(map_distance)
		for map_distance in distance_maps_for_san:
			if not map_distance.orbit.name in combine:
				combine[map_distance.orbit.name] = []
			combine[map_distance.orbit.name].append(map_distance)

		intersections = []
		for key in combine.keys():
			if len(combine[key]) > 1:
				intersections.append(combine[key])
		shortest_intersection = None
		if self.debug:
			print intersections
		for intersection in intersections:
			total_distance = intersection[0].distance + intersection[1].distance
			if shortest_intersection == None or total_distance < shortest_intersection:
				shortest_intersection = total_distance
		return shortest_intersection - 2


