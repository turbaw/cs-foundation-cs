import random

# --- Key Generation ---
def generate_key_pair(): 
    p = 211  # A larger prime to handle ASCII values
    g = 5    # Primitive root modulo p
    x = random.randint(1, p-2)  # Private key
    h = pow(g, x, p)  # Public key component used to calculate formula h=g^x mod p
    public_key = (p, g, h) #creates the public key as a tuple containing the values of p,g and h
    private_key = x # assigns the private key x to the variable private_key
    return public_key, private_key #returns both the public and private key 


# --- Encryption ---
def encrypt(public_key, message):
    p, g, h = public_key #unpacks the public key tuble into three variables which are p for prime
                            # modulus and g the primitive root modulu 
                            #and h the public key component
    ciphertext = [] #initializes an empty list called cipher text and it will hold the encrypted form of the message 

    for char in message:  # Encrypt each character
        m = ord(char)  # Convert character to ASCII
        k = random.randint(1, p-2)  # Random ephemeral key
        c1 = pow(g, k, p) #this calculates the firs part of the cipher text
        c2 = (m * pow(h, k, p)) % p # calculates the second part of cipher text c2 = 
        ciphertext.append((c1, c2))  # Append tuple (c1, c2) for each character

    return ciphertext


# --- Decryption ---
def decrypt(private_key, ciphertext, p):
    decrypted_message = "" #initialize empty string which will hold the final result of the decrypted text

    for c1, c2 in ciphertext:  # Decrypt each tuple (c1, c2)
        s = pow(c1, private_key, p) #Calculates s=c1^textprivatekey\ mod p
        s_inv = pow(s, p-2, p)  # Modular inverse of s
        m = (c2 * s_inv) % p #calculate the original ASCII value of the character that was encrypted
        decrypted_message += chr(m)  # Convert ASCII value back to character

    return decrypted_message


# --- Main Process ---
# Key Generation
public_key, private_key = generate_key_pair()
print("Public Key:", public_key)
print("Private Key:", private_key)
    
# Encrypting a Message
message = "farid is very tob "  # Message to encrypt
ciphertext = encrypt(public_key, message)  # Encrypt the message

# Decrypting the Message
decrypted_message = decrypt(private_key, ciphertext, public_key[0])  # Decrypt the ciphertext
print("Decrypted Message:", decrypted_message)
