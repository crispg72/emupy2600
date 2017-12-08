from emupy2600.memory import Memory


def test_load_rom():
	sequence = bytearray(b'\x01\x03\x05\x04\x02')
	test_rom = bytearray(b'\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00')
	test_rom += sequence
	mem = Memory(len(test_rom), test_rom)

	assert mem.buffer[16:16+len(sequence)] == sequence