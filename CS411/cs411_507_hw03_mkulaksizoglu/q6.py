def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
# a × b  mod q  = r
a_1  = 2700926558
b_1  = 967358719
q_1  = 3736942861

a_2  = 1759062776
b_2  = 1106845162
q_2  = 3105999989

a_3  = 2333074535
b_3  = 2468838480
q_3  = 2681377229 

Q= q_1 * q_2 * q_3

a = [a_1*b_1,a_2*b_2,a_3*b_3]
N= [Q//q_1,Q//q_2,Q//q_3]
M= [modinv(N[0],q_1),modinv(N[1],q_2),modinv(N[2],q_3)]
R=0
for i in range(3):
    temp= a[i] * N[i] * M[i]
    R+=temp
R= R%Q
print("R is ",R)
print("r1 is (R%q1))", R % q_1)
print("r2 is (R%q2) ", R % q_2)
print("r3 is (R%q3) ", R % q_3)

'''
FOR COMPARISON
print((a_1*b_1) % q_1)
print((a_2*b_2) % q_2)
print((a_3*b_3) % q_3)
'''