

class tia(object):

	def __init__(self):
		self.background_colour = 0
		self.write_fn = {
			0x02: self.write_wsync
			0x09: self.write_colubk
		}

	def write_colubk(self, value):
		self.background_colour = value

	def write(self, address, value):
		register = address & 0xff
		self.write_fn[register](value)
