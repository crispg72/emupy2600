import pytest
from emupy2600.tia import Tia


def test_clear_vblank():
    tia = Tia()

    # Set some crazy values
    tia.current_scan_line = 1001
    tia.current_line_clk = 999

    # write 0 to VBLANK (0x01)
    tia.write(0x01, 0)
    assert tia.current_scan_line == 0
    assert tia.current_line_clk == 0


def test_vertical_blanking():
    tia = Tia()

    tia.current_scan_line = 999
    tia.write(0x01, 0) # VBLANK 0
    tia.write(0x00, 2) # VSYNC 2
    
    tia.write(0x02, 2)
    tia.write(0x02, 2)
    tia.write(0x02, 2) # WSYNC x 3

    tia.write(0x00, 0) # VSYNC 0

    assert tia.current_line_clk == 0
    assert tia.current_scan_line == 3
    assert not tia.in_vsync
