import random

# --- Key Generation ---
def generate_key_pair():
    # Step 1: Choose a large prime number p (for simplicity, using a small prime)
    p = 211
    
    # Step 2: Select a generator g (primitive root modulo p)
    g = 5  # A small generator; in practice, choose a valid primitive root
    
    # Step 3: Generate the private key x
    x = random.randint(1, p-2)  # Random private key, 1 <= x <= p-2
    
    # Step 4: Compute the public key component h
    h = pow(g, x, p)  # h = (g^x) mod p
    
    # Step 5: Define the keys
    public_key = (p, g, h)
    private_key = x
    
    return public_key, private_key


# --- Encryption ---
def encrypt(public_key, message):
    p, g, h = public_key
    
    # Step 2: Choose a random ephemeral key k
    k = random.randint(1, p-2)  # Random k, 1 <= k <= p-2
    
    # Step 3: Compute the first part of the ciphertext (c1)
    c1 = pow(g, k, p)  # c1 = (g^k) mod p
    
    # Step 4: Compute the second part of the ciphertext (c2)
    m = message % p  # Message should be modulo p
    c2 = (m * pow(h, k, p)) % p  # c2 = (m * (h^k)) mod p
    
    # Step 5: Define the ciphertext
    ciphertext = (c1, c2)
    
    return ciphertext


# --- Decryption ---
def decrypt(private_key, ciphertext, p):
    c1, c2 = ciphertext
    x = private_key
    
    # Step 2: Compute the shared secret s
    s = pow(c1, x, p)  # s = (c1^x) mod p
    
    # Step 3: Compute the modular inverse of s
    s_inv = pow(s, p-2, p)  # s_inv = s^-1 mod p (Fermat's Little Theorem)
    
    # Step 4: Recover the original message
    m = (c2 * s_inv) % p  # m = (c2 * s_inv) mod p
    
    return m


# --- Main Process ---
# 1. Key Generation
public_key, private_key = generate_key_pair()
print("Public Key:", public_key)
print("Private Key:", private_key)

# 2. Encrypting a Message
message = 15  # Example message
ciphertext = encrypt(public_key, message)
print("Ciphertext (c1, c2):", ciphertext)

# 3. Decrypting the Message
decrypted_message = decrypt(private_key, ciphertext, public_key[0])
print("Decrypted Message:", decrypted_message)
