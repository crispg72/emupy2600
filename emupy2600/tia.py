

class tia(object):

	def __init__(
		self, mode = 'PAL',
		display_driver = None):

        if mode == "PAL":
            self.total_scan_lines = 312
            self.clocks_per_line = 228
        else:
            self.total_scan_lines = 262
            self.clocks_per_line = 228

		self.background_colour = 0
		self.current_scan_line = 0
		self.current_line_clk = 0
		self.write_fn = {
			0x02: self.write_wsync
			0x09: self.write_colubk
		}

	def write_colubk(self, value):
		self.background_colour = value

	def write_wsync(self, value):
		if self.current_scanline_visible():
			self.display_driver.draw_horizontal_line(
				self.clocks_per_line - self.current_line_clk,
				228,
				self.current_scan_line
			)

		self.current_line_clk = 0
		self.current_scanline += 1

	def write(self, address, value):
		register = address & 0xff
		self.write_fn[register](value)

	def current_scanline_visible(self):
		return self.current_scan_line > 40 and
			   self.current_scan_line < 232