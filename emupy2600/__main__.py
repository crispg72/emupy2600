import sys

from emupy6502.cpu6502 import Cpu6502
from emupy2600.system import System
from emupy2600.displaydriver_pygame import DisplayDriverPyGame


def main(rom_filename):
	cpu = Cpu6502()

	with open(rom_filename, 'rb') as rom_file:
		rom = rom_file.read()

	system = System(
		cpu,
		rom,
		DisplayDriverPyGame(180,200))

	system.run()

if __name__ == "__main__":
	main(sys.argv[1])


