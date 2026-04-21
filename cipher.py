
def encrypt(data : str, seed: int):
    byte_data = bytearray(data, 'utf-8')
    encrypted_data: bytearray = bytearray(len(byte_data))
    i: int = 0
    for ch in byte_data:
        encrypted_data[i] = ch + seed
        i += 1
    return encrypted_data.decode('utf-8')


def encrypt_file(path: str, seed) -> str:
    f = open(path)
    data = f.read()
    encrypted_data = encrypt(data, seed)
    f.close()
    return encrypted_data

