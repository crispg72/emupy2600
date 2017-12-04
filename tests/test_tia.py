import pytest
from emupy2600.tia import Tia


def test_set_single_line_colour():
    tia = Tia()

    # Set some crazy values
    tia.current_scan_line = 1001
    tia.current_line_clk = 999

    # write 0 to VBLANK (0x01)
    tia.write(0x01, 0)
    assert tia.current_scan_line == 0
    assert tia.current_line_clk == 0
