import pytest
from unittest.mock import MagicMock

from emupy2600.palette import PAL_Colours, NTSC_Colours


@pytest.mark.parametrize("palette", [
    (PAL_Colours()),
    (NTSC_Colours())
])
def test_palettes(palette):

    assert len(palette.palette_lookup) == 128

    colours = [palette.IndexToRGB(col) for col in range(0, 255, 2)]
    assert len(colours) == 128

    lengths = [len(c) for c in colours]
    assert lengths[0] == 3
    assert lengths[1:] == lengths[:-1]
