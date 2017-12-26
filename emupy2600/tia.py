
from emupy2600.palette import PAL_Colours, NTSC_Colours

class Tia(object):

    def __init__(
        self, mode = 'PAL',
        display_driver = None, 
        cpu = None):

        self.display_driver = display_driver
        self.cpu = cpu
        if mode == "PAL":
            self.total_scan_lines = 312
            self.palette = PAL_Colours()
        else:
            self.total_scan_lines = 262
            self.palette = NTSC_Colours()

        self.cpuclocks_per_line = 76

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
        self.background_colour = self.palette.IndexToRGB(value)

    def write_wsync(self, value):
        if self.current_scanline_visible():
            self.display_driver.draw_horizontal_line(
                self.get_current_raster_x(),
                160,
                self.current_scan_line - 40,
                self.background_colour
            )

        self.current_line_clk = 0
        self.current_scan_line += 1

    def write_vsync(self, value):
        self.in_vsync = value

    def write_vblank(self, value):
        if value & 0x02:
            self.in_vblank = True
            self.display_driver.end_frame()
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
            self.current_scan_line >= 40 and
            self.current_scan_line < 232
        )

    def get_current_raster_x(self):
        return int( 
            (
            float(self.cpu.total_cycles - 
                self.current_line_clk) / 
            float(self.cpuclocks_per_line)) * 160
        )