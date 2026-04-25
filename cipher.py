
def shift_char(ch, n):
    return chr(ord(ch)+n)

def encrypt(data : str, seed: int):
    encrypted_data: str = ''
    for ch in data:
        encrypted_data += shift_char(ch,seed)
    return encrypted_data


def decrypt(data: str, seed: int):
    return encrypt(data, -seed)


def encrypt_file(path: str, seed) -> str:
    f = open(path)
    data = f.read()
    encrypted_data = encrypt(data, seed)
    f.close()
    return encrypted_data

