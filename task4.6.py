# Furniture:
# Household type, total area and furniture name listThe new house has no furniture at all.
# Furniture has a name and area, of whichBed: 4 square metersWardrobe: 2 square metersTable:
# 1.5 square meters
# Add the above three pieces of furniture to the house
# When printing a house, output is required: household type, total area, remaining area,
# furniture name list.

class Bedroom:
	def __init__(self,household,bed=4,wardrobe=2,table=1.5):
		self.household=household
		self.bed=bed
		self.wardrobe=wardrobe
		self.table= table

	def total_square(self):
		global total_area
		total_area=self.bed+self.wardrobe+self.table



	def result(self):
		print('Тип комнаты:',self.household,',общая площадь комнаты:',total_area,'кв,у кровати',self.bed,'кв,у гардероба',self.wardrobe,'кв у стола',self.table,'кв')

Bek=Bedroom('спалня студента')
Bek.total_square()
Bek.result()