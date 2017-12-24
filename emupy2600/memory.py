

class Memory(object):

    def __init__(self, size, tia, rom = None):

        if rom:
            org = rom[0] + (rom[1] << 8)
            self.buffer = bytearray(size + org)
            for b in range(2, size):
                self.buffer[org] = rom[b]
                org += 1
        else:
            self.buffer = bytearray(size)

        self.tia = tia


    def read(self, address):
        return self.buffer[address]

    def write(self, address, value):
        if address < 0x80:
            self.tia.write(address, value)
        else:
            self.buffer[address] = value
