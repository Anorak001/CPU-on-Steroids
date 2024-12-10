import random
import math

def generate_key_pair(bits=8):
    # Step 1: Choose two large prime numbers, p and q
    p = generate_prime(bits)
    q = generate_prime(bits)

    # Step 2: Compute n (modulus) and phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Step 3: Choose e (public exponent) such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = choose_public_exponent(phi_n)

    # Step 4: Compute d (private exponent) such that d * e ≡ 1 (mod phi(n))
    d = mod_inverse(e, phi_n)

    return ((n, e), (n, d))

def choose_public_exponent(phi_n):
    # A common choice for e due to its properties
    e = 65537
    while math.gcd(e, phi_n) != 1:
        e += 2
    return e

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(message, public_key):
    n, e = public_key
    m = int.from_bytes(message.encode('utf-8'), 'big')
    c = pow(m, e, n)
    return c


def decrypt(ciphertext, private_key):
    n, d = private_key
    m = pow(ciphertext, d, n)
    byte_result = m.to_bytes((m.bit_length() + 7) // 8, 'big')

    try:
        decoded_message = byte_result.decode('utf-8')
        return decoded_message
    except UnicodeDecodeError as e:
        print(f"Decoding error: {e}")
        print("Bytes representation:", byte_result)
        return None


# Example usage:
private_key, public_key = generate_key_pair(bits=16)

message_to_encrypt = "Hello, RSA!"
ciphertext = encrypt(message_to_encrypt, public_key)
print("Encrypted:", ciphertext)

decrypted_message = decrypt(ciphertext, private_key)
print("Decrypted:", decrypted_message)
