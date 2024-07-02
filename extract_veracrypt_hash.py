import struct
import sys

def read_veracrypt_header(filename):
    with open(filename, 'rb') as f:
        header = f.read(512)
        salt = header[64:96]
        iterations = struct.unpack('<I', header[128:132])[0]
        return salt, iterations

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <veracrypt_volume>")
        sys.exit(1)

    salt, iterations = read_veracrypt_header(sys.argv[1])
    print(f"Salt: {salt.hex()}")
    print(f"Iterations: {iterations}")
