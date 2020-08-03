from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)

data = b'Mr.Natthapol  Nonthasri'
print('data: ', data)

ciphertext, tag = cipher.encrypt_and_digest(data)
print('Ci: ', ciphertext)

cipher = AES.new(key, AES.MODE_EAX, cipher.nonce)
data_de = cipher.decrypt_and_verify(ciphertext, tag)

print('Pi: ', data_de.decode('utf-8'))

# https://pycryptodome.readthedocs.io/en/latest/src/examples.html