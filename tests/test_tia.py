import pytest
from unittest.mock import MagicMock

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


def test_vertical_synch():
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


def test_vertical_blank():
    mock_display = MagicMock()
    mock_display.draw_horizontal_line = MagicMock()
    tia = Tia(display_driver = mock_display)

    tia.current_scan_line = 999
    tia.write(0x01, 0) # VBLANK 0
    tia.write(0x00, 2) # VSYNC 2
    
    tia.write(0x02, 2)
    tia.write(0x02, 2)
    tia.write(0x02, 2) # WSYNC x 3

    tia.write(0x00, 0) # VSYNC 0

    for c in range(0, 37):
        tia.write(0x02, 0) # WSYNC x 37

    assert tia.current_line_clk == 0
    assert tia.current_scan_line == 40
    assert not tia.in_vsync
    assert not tia.in_vblank
    assert not mock_display.draw_horizontal_line.called


def test_vertical_overscan():
    mock_display = MagicMock()
    mock_display.draw_horizontal_line = MagicMock()
    tia = Tia(display_driver = mock_display)

    tia.current_scan_line = 232
    tia.write(0x01, 0x2) # VBLANK ON

    for c in range(0, 30):
        tia.write(0x02, 0) # WSYNC x 30

    assert tia.current_line_clk == 0
    assert tia.current_scan_line == 262
    assert tia.in_vblank
    assert not mock_display.draw_horizontal_line.called
    assert mock_display.end_frame.called


def test_single_colour_line():
    mock_display = MagicMock()
    mock_display.draw_horizontal_line = MagicMock()
    mock_cpu = MagicMock()
    tia = Tia(
        display_driver = mock_display,
        cpu = mock_cpu
    )

    tia.current_scan_line = 40
    mock_cpu.total_cycles = 0

    tia.write(0x09, 2) # COLUBK 
    tia.write(0x02, 0) # WSYNC

    assert tia.current_line_clk == 0
    assert tia.current_scan_line == 41
    assert mock_display.draw_horizontal_line.called_once

    # Assume default PAL
    mock_display.draw_horizontal_line.assert_called_with(0, 160, 0, (40, 40, 40))
