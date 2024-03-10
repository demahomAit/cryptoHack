# Encrypted key in hexadecimal format
Crypted_key = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

# Convert the encrypted key from hexadecimal to bytes
Crypted_key_byt = bytes.fromhex(Crypted_key)

# Known string (partial plaintext)
string_connu = b"crypto{"

# Generate the key for XOR decryption
# XOR each byte of the encrypted key with the corresponding byte of the known string
# Append the ASCII value of "y" to the key
key = [a ^ b for (a, b) in zip(Crypted_key_byt, string_connu)] + [ord("y")]

# Initialize an empty list to store the decrypted bytes
flag = []

# Calculate the length of the key
t = len(key)

# Print the length of the key and the length of the encrypted key
print(t)
print(len(Crypted_key_byt))

# Decrypt the encrypted key using XOR with the generated key
for i in range(len(Crypted_key_byt)):
    flag.append(Crypted_key_byt[i] ^ key[i % t])

# Convert the decrypted bytes to characters and concatenate them to form the decrypted text
flag = ''.join(chr(o) for o in flag)

# Print the decrypted text
print(flag)
