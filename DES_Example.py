from des import DesKey

key0 = DesKey(b"some key")                  # for DES
key1 = DesKey(b"a key for TRIPLE")          # for 3DES, same as "a key for TRIPLEa key fo"
key2 = DesKey(b"a 24-byte key for TRIPLE")  # for 3DES
key3 = DesKey(b"1234567812345678REAL_KEY")  # for DES, same as "REAL_KEY"

# key0.is_single()  # -> True
# key1.is_triple()  # -> True
# key2.is_single()  # -> False
# key3.is_triple()  # -> False

data_en = key0.encrypt(b"any long message")  # -> b"\x14\xfa\xc2 '\x00{\xa9\xdc;\x9dq\xcbr\x87Q"
data_de = key0.decrypt(data_en)  # -> b"abc"

data_en_in = key0.encrypt(b"any long message", initial=0)
data_de_in = key0.decrypt(data_en_in, initial=0)

data_en_ins = key0.encrypt(b"any long message", initial=b"\0"*8)  # same as above
data_de_ins = key0.decrypt(data_en_in, initial=b"\0"*8)

msg = b'Mr.Natthapol  Nonthasri'
data_en_pd = key0.encrypt(msg, padding=True)  # -> b"%\xd1KU\x8b_A\xa6"
data_de_pd = key0.decrypt(data_en_pd, padding=True)

print('Data: ', msg)
print('Ci: ', data_en_pd)
print('Pi: ', data_de_pd)

# https://pypi.org/project/des/