
from emupy2600.memory import Memory
from emupy2600.tia import Tia


class System(object):

	def __init__(self, cpu, rom, display_driver):
		self.cpu = cpu
		self.cpu.registers.pc = rom[0] + (rom[1] << 8)
		self.tia = Tia(mode = 'NTSC', display_driver = display_driver)
		self.memory = Memory(len(rom), self.tia, rom)
		self.cpu.memory_controller = self.memory

	def signal(self):
		return False

	def run(self):
		self.cpu.run_until_signalled(self.signal)