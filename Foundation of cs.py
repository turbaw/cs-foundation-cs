import random

# --- Key Generation ---
def generate_key_pair():
    p = 211  # A larger prime to handle ASCII values
    g = 5    # Primitive root modulo p
    x = random.randint(1, p-2)  # Private key
    h = pow(g, x, p)  # Public key component
    public_key = (p, g, h)
    private_key = x
    return public_key, private_key


# --- Encryption ---
def encrypt(public_key, message):
    p, g, h = public_key
    ciphertext = []

    for char in message:  # Encrypt each character
        m = ord(char)  # Convert character to ASCII
        k = random.randint(1, p-2)  # Random ephemeral key
        c1 = pow(g, k, p)
        c2 = (m * pow(h, k, p)) % p
        ciphertext.append((c1, c2))  # Append tuple (c1, c2) for each character

    return ciphertext


# --- Decryption ---
def decrypt(private_key, ciphertext, p):
    decrypted_message = ""

    for c1, c2 in ciphertext:  # Decrypt each tuple (c1, c2)
        s = pow(c1, private_key, p)
        s_inv = pow(s, p-2, p)  # Modular inverse of s
        m = (c2 * s_inv) % p
        decrypted_message += chr(m)  # Convert ASCII value back to character

    return decrypted_message


# --- Main Process ---
# Key Generation
public_key, private_key = generate_key_pair()
print("Public Key:", public_key)
print("Private Key:", private_key)

# Encrypting a Message
message = "Farid is tob "  # Message to encrypt
ciphertext = encrypt(public_key, message)  # Encrypt the message

# Decrypting the Message
decrypted_message = decrypt(private_key, ciphertext, public_key[0])  # Decrypt the ciphertext
print("Decrypted Message:", decrypted_message)
