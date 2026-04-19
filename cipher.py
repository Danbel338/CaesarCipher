def ccipher(data : str, seed: int):
    byte_data = bytearray(data, 'utf-8')
    encrypted_data: bytearray = bytearray(len(byte_data))
    i: int = 0
    for ch in byte_data:
        encrypted_data[i] = ch + seed
        i += 1
    return encrypted_data.decode('utf-8')

