from Crypto.PublicKey import RSA


k1 = RSA.importKey( open('public3.pub', 'r').read() )
k2 = RSA.importKey( open('private3.pem', 'r').read() )

data = "hello world"

data = k1.encrypt(data,1)

print(data)

data = k2.decrypt(data)

print('\nAfter : ')
print(data)
