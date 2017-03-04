class ZeroFiller:


    def get_shell_code(self):
        return self.shell_code

    def get_padded_shell_code(self, padding_size):
        padding = bytearray([0x0 for x in range(0, padding_size)])
        unpadded_shell_code = bytearray(self.shell_code)
        unpadded_shell_code.extend(padding)
        return unpadded_shell_code

    def __init__(self):
        self.shell_code = bytearray([0x42,0x52,0x55,0x4E,0x4F,0x21,0x21,0x21,0x21,0x21,0x21,0x21,0x21,0x21,0x21,0x21])

