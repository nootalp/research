class Encrypt:

    @staticmethod
    def convert_raw_string_to_byte_array(raw_string):
        if len(raw_string) % 2 != 0:
            raise ValueError("String should have an even number of characters.")

        byte_count = len(raw_string) // 2
        byte_array = bytearray()

        for i in range(byte_count):
            byte_str = raw_string[i * 2: i * 2 + 2]
            byte_array.append(int(byte_str, 16))

        return byte_array

    @staticmethod
    def encrypt_decrypt_byte_array(byte_array):
        return bytearray(byte ^ 54 for byte in byte_array)

    @staticmethod
    def print_byte_array(byte_array, filename):
        with open(filename, "w") as file:
            file.write("byte[] shellcode = new byte[{}] {{\n    ".format(len(byte_array)))
            for i, byte in enumerate(byte_array):
                if i == len(byte_array) - 1:
                    file.write("0x{:02X}".format(byte))
                else:
                    file.write("0x{:02X}, ".format(byte))
                    if (i + 1) % 16 == 0:
                        file.write("\n    ")
            file.write("\n};\n")
