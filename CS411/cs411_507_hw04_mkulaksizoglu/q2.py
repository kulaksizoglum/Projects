from RSA_OAEP import *
c=15563317436145196345966012870951355467518223110264667537181074973436065350566
e= 65537
N=73420032891236901695050447655500861343824713605141822866885089621205131680183


flag=1
for m in range(1000, 9999):
    if flag==0:
        break
    for R in range(2**(k0-1), 2**k0-1):
        possibleC = RSA_OAEP_Enc(m, e, N, R)
        if c==possibleC :
            print("Secret code is:",m)
            flag=0
            break
   