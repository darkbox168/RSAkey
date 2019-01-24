from Crypto.PublicKey import RSA
from fractions import gcd

###following code reference from https://goo.gl/xmEEvF
def egcd(a, b):
	x,y,u,v = 0,1,1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	return x
###


publickeys = []
for i in range(12):
	publickeys.append( RSA.importKey( open('public'+str(i+1)+'.pub', 'r').read() ) )

for j in range(11):
	for k in range(11-j):
		if( gcd(publickeys[j].n,publickeys[j+k+1].n) != 1 ):
			gcdn = 	gcd(publickeys[j].n,publickeys[j+k+1].n)
			a = publickeys[j].n / gcdn 
			c = publickeys[j+k+1].n / gcdn
			phi1 = (a-1)*(gcdn-1)
			phi2 = (c-1)*(gcdn-1) 
			print( 'common divisor found in public key ' + str(j+1) + ' and ' + str(j+k+2))
			d1 = egcd( publickeys[j].e , phi1 ) % (phi1)
			d2 = egcd( publickeys[j+k+1].e , phi2 ) % (phi2)
			tup1 = [publickeys[j].n, publickeys[j].e, d1]
			tup2 = [publickeys[j+k+1].n, publickeys[j+k+1].e, d2]
			privatekey1 = RSA.construct(tup1)
			privatekey2 = RSA.construct(tup2)
			print('create private key ' + str(j+1) )
			f1 = open('private'+str(j+1)+'.pem' , 'w')
			f1.write(privatekey1.exportKey('PEM'))
			f1.close()
			print('create private key ' + str(j+k+2) )
			f2 = open('private'+str(j+k+2)+'.pem' , 'w')
			f2.write(privatekey2.exportKey('PEM'))
			f2.close()

