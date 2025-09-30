import math
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
def modinv(a, m):
    if a < 0:
        a = m+a
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
    
def solution(gcd,a,b,n,number):
    a= a//gcd
    b= b//gcd
    n= n//gcd
    inv=modinv(a,n)
    x=(b*inv)% n
    if gcd==1:
        print(x)
    else:
        for i in range(gcd):
            print(x + n*i)


    

n1 = 2163549842134198432168413248765413213216846313201654681321666
a1 = 790561357610948121359486508174511392048190453149805781203471
b1 = 789213546531316846789795646513847987986321321489798756453122

n2=  3213658549865135168979651321658479846132113478463213516854666
a2=  789651315469879651321564984635213654984153213216584984653138
b2=  798796513213549846121654984652134168796513216854984321354987

n3 = 5465132165884684652134189498513211231584651321849654897498222
a3 = 654652132165498465231321654946513216854984652132165849651312
b3 = 987965132135498749652131684984653216587986515149879613516844
 
n4= 6285867509106222295001894542787657383846562979010156750642244
a4 = 798442746309714903987853299207137826650460450190001016593820
b4 = 263077027284763417836483408268884721142505761791336585685868

gcd1= math.gcd(a1,n1)
gcd2= math.gcd(a2,n2)
gcd3= math.gcd(a3,n3)
gcd4= math.gcd(a4,n4)

print("GCD1 is", gcd1)
print("B1 MOD GCD1 is", b1%gcd1)
inv1= modinv(a1,n1)
x=(b1*inv1)% n1

print("There is a solution which is ",x)
print("GCD2 is", gcd2)
print("B2 MOD GCD2 is", b2%gcd2)
print("gcd2 does not divide b2---> There is no solution")
print("GCD3 is", gcd3)
print("B3 MOD GCD3 is", b3%gcd3)
print("BECAUSE GCD3 DIVIDES B3 THERE ARE 2  SOLUTIONS")
solution(gcd3,a3,b3,n3,3)
print("GCD4 is", gcd4)
print("B4 MOD GCD4 is", b4%gcd4)
print("BECAUSE GCD4 DIVIDES B4 THERE ARE 4  SOLUTIONS")
solution(gcd4,a4,b4,n4,4)





