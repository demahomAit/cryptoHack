# Encoded data in hexadecimal format
encoded_data = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

# Function to decrypt data using XOR with a given key
def xor_decrypt(data, key):
    return bytes([byte ^ key for byte in data])

# Iterate through all possible key values (0x00 to 0xFF)
for key in range(256):
    # Decrypt the encoded data using the current key
    decrypted = xor_decrypt(encoded_data, key)
    # Check if all bytes of the decrypted data are printable characters or space
    if all(chr(byte).isprintable() or byte == 0x20 for byte in decrypted):
        # If the decrypted data consists of printable characters, print the key and decrypted data
        print(f"Key: {key}, Decrypted data: {decrypted}")
