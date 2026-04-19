import sys
import cipher

def main():
    print("CAESAR CIPHER\n")
    encrypted_string: str = cipher.ccipher("HOLA", 2)
    print(encrypted_string)
    return 0

if __name__ == '__main__':
    sys.exit(main())
