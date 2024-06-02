import argparse
from package.class_encrypt import Encrypt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt and decrypt byte array from a file")
    parser.add_argument("filename", help="Path to the file containing the hexadecimal string")

    args = parser.parse_args()

    with open(args.filename, "r") as file:
        content = file.read().strip()

    byte_array = Encrypt.convert_raw_string_to_byte_array(content)
    encrypted_byte_array = Encrypt.encrypt_decrypt_byte_array(byte_array)

    Encrypt.print_byte_array(byte_array, "shell-dec.txt")
    Encrypt.print_byte_array(encrypted_byte_array, "shell-enc.txt")
