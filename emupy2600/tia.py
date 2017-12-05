

class Tia(object):

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
            0x00: self.write_vsync,
            0x01: self.write_vblank,
            0x02: self.write_wsync,
            0x09: self.write_colubk,
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
        self.current_scan_line += 1

    def write_vsync(self, value):
        self.in_vsync = value

    def write_vblank(self, value):
        if value & 0x02:
            self.in_vblank = True
        elif not value:
            # start of vblank (ie top of screen)
            self.in_vblank = False
            self.current_scan_line = 0
            self.current_line_clk = 0

    def write(self, address, value):
        register = address & 0x7f
        self.write_fn[register](value)

    def current_scanline_visible(self):
        return (
            self.current_scan_line > 40 and
            self.current_scan_line < 232
        )