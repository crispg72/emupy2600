

class Memory(object):

	def __init__(self, size, rom = None):

		if rom:
			org = rom[0] + (rom[1] << 8)
			self.buffer = bytearray(size + org)
			for b in range(2, size):
				self.buffer[org] = rom[b]
				org += 1
		else:
			self.buffer = bytearray(size)
