import math

from sympy.ntheory import factorint

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m



N = 9244432371785620259
C = 655985469758642450
e = 2**16+1

p,q = factorint(N)
print(f"p is {p}")
print(f"q is {q}")

phi_n= (p-1)*(q-1)

d= modinv(e,phi_n)

m= pow(C,d,N)

print ("\n\nMessage: ", m.to_bytes((m.bit_length()+7)//8, byteorder='big'))

