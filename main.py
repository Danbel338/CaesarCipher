import sys
import cipher

def main():
    print("CAESAR CIPHER\n")
    encrypted_string: str = cipher.encrypt_file("README.md", 1)
    print(encrypted_string)
    return 0

if __name__ == '__main__':
    sys.exit(main())
