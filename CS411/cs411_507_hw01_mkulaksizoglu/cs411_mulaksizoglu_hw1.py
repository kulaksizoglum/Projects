import math
import random
import fractions

def style(ctext):
    #ctext= ctext.replace(" ", "")
    ctext= ctext.replace(",", "")
    ctext= ctext.replace("-","")
    ctext= ctext.replace(".","")
    ctext= ctext.replace(";","")
    ctext= ctext.replace("’","")
    return ctext

def subtextFunc(text,start):
    subtext=text[start::5]
    return subtext

def Affine_Dec(ptext, key):
    plen = len(ptext)
    ctext = ''
    for i in range (0,plen):
        letter = ptext[i]
        if letter in lowercase:
            poz = lowercase[letter]
            poz = (key.gamma*poz+key.theta)%26
            #print poz
            ctext += inv_lowercase[poz]
        elif letter in uppercase:
            poz = uppercase[letter]
            poz = (key.gamma*poz+key.theta)%26
            ctext += inv_uppercase[poz]
        else:
            ctext += ptext[i]
    return ctext

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

lowercase = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8,
         'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16,
         'r':17, 's':18,  't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24,
         'z':25}

inv_lowercase = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i',
         9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q',
         17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y',
         25:'z'}

uppercase ={'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8,
         'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16,
         'R':17, 'S':18,  'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24,
         'Z':25}

inv_uppercase = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
                 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P',
                 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X',
                 24:'Y', 25:'Z'}

def frequency_test(text):
    frequency_dic ={}
    for i in text:
        i=i.lower()
        if i in frequency_dic:
           frequency_dic[i]+=1
        else:
           frequency_dic[i]=1
    return frequency_dic

def dec_vigenereCipher(ctext,key):
    clen = len(ctext)
    ptext=""
    x=0

    for i in range(clen):
        letter = ctext[i]
        if letter in uppercase:
            add= uppercase[key[x%5]]
            poz= (uppercase[letter] + add) %26
            ptext += inv_uppercase[poz]
            x+=1

        
        else:
            ptext += ctext[i]
            
    return ptext


def coincidence(ctext,subtext):
    count=0
    for i in range(len(ctext)):
        if ctext[i]==subtext[i]:
            count+=1
    return count


def shift_dec(ctext):
    
    for i in range(0,26):
        ptext=''
        for x in range(len(ctext)):
            val= uppercase[ctext[x]]
            poz=(val+i)%26
            ptext += inv_uppercase[poz]
        print("Decription for key= ",i,"is",ptext)
"""
print("-----------QUESTION 1------------")

ctext="NLPDLC"
shift_dec(ctext)


print ("By checking the output of the caesar decryption function decrption key=15 and encrption key= 11, the actual word is CAESAR /n ")
"""

"""

print("-----------QUESTION 2------------")

ctext="J gjg mxa czjq ayr arpa. J ulpa cxlmg ayerr ylmgerg rqrwrm hzdp ax gx ja hexmn."
ctext_noblank= ctext.replace(" ", "")
frequency_dic = frequency_test(ctext_noblank)
for char, count in frequency_dic.items():
    print(f"'{char}': {count}")

print("Most frequent letter is 'a' or 'r' with 8 occurrences one of them. One of them will point to letter 'xt',I will start with a, <t>=19 <a>=0 corresponding equation is 0=23.α+ β mod(26).")

solutions = []

for alpha in (1,3,5,7,9,11,15,17,19,21,23,25):
    for beta in range(26):
        if (19 * alpha + beta) % 26 == 0:
            gamma = modinv(alpha, 26) # you can compute decryption key from encryption key
            theta = 26-(gamma*beta)%26
            solutions.append((alpha, beta,gamma,theta))

print("Possible solutions for alpha and beta:")
for alpha, beta,gamma,theta in solutions:
    print(f"Alpha (α): {alpha}, Beta (β): {beta}, Gamma: {gamma} , Theta: {theta} ")

class key(object):
    alpha=0
    beta=0
    gamma=0
    theta=0
for alpha, beta,gamma,theta in solutions:
    key.alpha = theta
    key.beta = beta
    key.gamma = gamma # you can compute decryption key from encryption key
    key.theta = theta
    dtext={Affine_Dec(ctext,key)}
    print(f"Decryption for key alpha: {alpha} , beta {beta} , gamma {gamma} , theta {theta} is {dtext} ")

print("SOLUTION FOUND!!! Decryption with key alpha: 11 , beta 25 , gamma 19 , theta 19 is successfully correct. Thus, I stop calculation for the possibility of 'r' points to 't'")
print("The plaintext is I did not fail the test. I just found three hundred eleven ways to do it wrong.")
"""




"""

print("---------------------QUESTION 7--------------------------------")

ctext="FNZ FFZZMLQQZVO GAXXH PZ UPU QXGIHU UY NWJXR AHBDLPOMK YOUPZM,VOZAYCD. J TGQH B XUIJJZM ARS XOAH, BZJ D JP AT GLWUTB LO EVDWF AL GRHUI.OKPGMC L NME IRU NKGLFHK DQ UTK JUEQX JI UTK PQJHKMVF, KKO L MABZ WIQYOLDWE GLUFRZ OFMBZV BE ZCHZ AVZQ JZ YKUJZM. D OPHK OKF NRPH TWE, DOPHK NRNQ VZRQXK, RKPY UIH MABZV ZAA FQPI YJPFFOHHT IOOKPGZ FQPIOIJ XTE.D OPHK NRNQ MMHBF JZHEE JJQF NE HHO, FNJXHT O’QH MATB FFMYZG QQXCDQEZJ KBHK ADJFN DQ UTKH, BFF LMRN ARY KBNOO ROQ’Y CHBDZ KUJLKN WIQS. CHSQZCHZ TGQH CDUPJIF ZCH TAAK IPD EJX, FMZ DW, JF CDOM PU TRV SUJG. JF’YALSEZ-MDUQ YJXQ, FNZB LZUR KPI ZJ PBWK DW IQXZ. L XMTO WP FXVYFX OIHVDUKH, BXEJVIM, O NKBXR NHU ALA ISAS CHSQ. GIG ZQZ D NOAC OKBF O VP PZRTJPUTB WP M MMDWQEVUE, NAO LU’E G HRTF VMHDUUPV HDGQHZMXY, WIMZ’NZIMZ DW JE. VMHDUUPV BDK OKF PKVG UTGO OJQ ZCHSQ, KQHSK YOROQ UQHSFNZP TBKVNT AL NXDT HPUOUTB OJRK DQ UTK KDTF, UA VVON KDTEOJQBFK ADJFNDQ UTKDU XAXF, WIQOM WSGZC, WIQOM VUDABJMQ GIG UTKDU TOOZQDQ, ZCDUU QIRX U YCDMX LVOM AT OKF SXJXOP GIG LUYN WIAYZ VUATZV BZJ RHFB UQHSFNZP; UTUPJI U’S XROHOIFFP OI PZ TKVUU FNVW JF’Y GROS HZHO ZUOKJZM WXU MMMDWQEVUE. MTY L TTGGO OAZ RHFB LMRN PKNSBUX, WXU EOHSMK HZFBGYZ LTTGGO CQ NVSQK OI PZ FKVUT, U YCDMX YOHFB ST VPGR DQ FYUOLPZ. O GRWQZCH TFOXNZ XKVYFE OI VQDOIJ, UTK WOVQ YFB - UTGO’V BXR DW JE. OO’V OAZ VPBFZZU PR OIWFXRZFU AX GRHUI, DW’T XUQLOS CDWI ATZ’V JZYDGF, IOOK PZK’NVUASVFI"
ctext1= " " +ctext
ctext2= " " +ctext1
ctext3= " " +ctext2
ctext4= " " +ctext3
ctext5= " " +ctext4
ctext6= " " +ctext5
ctext7= " " +ctext6
ctext8= " " +ctext7
ctext9= " " +ctext8
ctext10= " " +ctext9



ctext= style(ctext)
ctext1= style(ctext1)
ctext2= style(ctext2)
ctext3= style(ctext3)
ctext4= style(ctext4)
ctext5= style(ctext5)
ctext6= style(ctext6)
ctext7= style(ctext7)
ctext8= style(ctext8)
ctext9= style(ctext9)
ctext10= style(ctext10)

print("Coincidence in shift= 1", coincidence(ctext,ctext1))
print("Coincidence in shift= 2", coincidence(ctext,ctext2))
print("Coincidence in shift= 3", coincidence(ctext,ctext3))
print("Coincidence in shift= 4", coincidence(ctext,ctext4))
print("Coincidence in shift= 5", coincidence(ctext,ctext5))
print("Coincidence in shift= 6", coincidence(ctext,ctext6))
print("Coincidence in shift= 7", coincidence(ctext,ctext7))
print("Coincidence in shift= 8", coincidence(ctext,ctext8))
print("Coincidence in shift= 9", coincidence(ctext,ctext9))
print("Coincidence in shift= 10", coincidence(ctext,ctext10))

print("According to coincidence test most probably the key length is 5.")

ctext= ctext.replace(" ", "")
subtext1=subtextFunc(ctext,0)
subtext2=subtextFunc(ctext,1)
subtext3=subtextFunc(ctext,2)
subtext4=subtextFunc(ctext,3)
subtext5=subtextFunc(ctext,4)
frequency_dic1=frequency_test(subtext1)
for char, count in frequency_dic1.items():
    print(f"'{char}': {count}")
print("if q is the most frequent it is pointing to e --> e.key = 12 d.key= 14")
print("-----------------------------------------------------")
frequency_dic2=frequency_test(subtext2)
for char, count in frequency_dic2.items():
    print(f"'{char}': {count}")
print("if k is the most frequent it is pointing to e --> e.key = 18 d.key= 6")
print("-----------------------------------------------------")
frequency_dic3=frequency_test(subtext3)
for char, count in frequency_dic3.items():
    print(f"'{char}': {count}")
print("if  z is the most frequent it is pointing to e --> e.key =  21 d.key= 5")
print("-----------------------------------------------------")

frequency_dic4=frequency_test(subtext4)
for char, count in frequency_dic4.items():
    print(f"'{char}': {count}")
print("if  z is the most frequent it is pointing to e --> e.key =  23 d.key= 3")
print("-----------------------------------------------------")

frequency_dic5=frequency_test(subtext5)
for char, count in frequency_dic5.items():
    print(f"'{char}': {count}")
print("if  f is the most frequent it is pointing to e --> e.key =  1 d.key= 25")
print("-----------------------------------------------------")

ctext="FNZ FFZZMLQQZVO GAXXH PZ UPU QXGIHU UY NWJXR AHBDLPOMK YOUPZM,VOZAYCD. J TGQH B XUIJJZM ARS XOAH, BZJ D JP AT GLWUTB LO EVDWF AL GRHUI.OKPGMC L NME IRU NKGLFHK DQ UTK JUEQX JI UTK PQJHKMVF, KKO L MABZ WIQYOLDWE GLUFRZ OFMBZV BE ZCHZ AVZQ JZ YKUJZM. D OPHK OKF NRPH TWE, DOPHK NRNQ VZRQXK, RKPY UIH MABZV ZAA FQPI YJPFFOHHT IOOKPGZ FQPIOIJ XTE.D OPHK NRNQ MMHBF JZHEE JJQF NE HHO, FNJXHT O’QH MATB FFMYZG QQXCDQEZJ KBHK ADJFN DQ UTKH, BFF LMRN ARY KBNOO ROQ’Y CHBDZ KUJLKN WIQS. CHSQZCHZ TGQH CDUPJIF ZCH TAAK IPD EJX, FMZ DW, JF CDOM PU TRV SUJG. JF’YALSEZ-MDUQ YJXQ, FNZB LZUR KPI ZJ PBWK DW IQXZ. L XMTO WP FXVYFX OIHVDUKH, BXEJVIM, O NKBXR NHU ALA ISAS CHSQ. GIG ZQZ D NOAC OKBF O VP PZRTJPUTB WP M MMDWQEVUE, NAO LU’E G HRTF VMHDUUPV HDGQHZMXY, WIMZ’NZIMZ DW JE. VMHDUUPV BDK OKF PKVG UTGO OJQ ZCHSQ, KQHSK YOROQ UQHSFNZP TBKVNT AL NXDT HPUOUTB OJRK DQ UTK KDTF, UA VVON KDTEOJQBFK ADJFNDQ UTKDU XAXF, WIQOM WSGZC, WIQOM VUDABJMQ GIG UTKDU TOOZQDQ, ZCDUU QIRX U YCDMX LVOM AT OKF SXJXOP GIG LUYN WIAYZ VUATZV BZJ RHFB UQHSFNZP; UTUPJI U’S XROHOIFFP OI PZ TKVUU FNVW JF’Y GROS HZHO ZUOKJZM WXU MMMDWQEVUE. MTY L TTGGO OAZ RHFB LMRN PKNSBUX, WXU EOHSMK HZFBGYZ LTTGGO CQ NVSQK OI PZ FKVUT, U YCDMX YOHFB ST VPGR DQ FYUOLPZ. O GRWQZCH TFOXNZ XKVYFE OI VQDOIJ, UTK WOVQ YFB - UTGO’V BXR DW JE. OO’V OAZ VPBFZZU PR OIWFXRZFU AX GRHUI, DW’T XUQLOS CDWI ATZ’V JZYDGF, IOOK PZK’NVUASVFI"

print("The final enycrption key is -MGVDB- and the decrpytion key is -OUFXZ-")
ptext=dec_vigenereCipher(ctext,"OUFXZ")
print("The plaintext is: ",ptext)
"""



"""
print("---------------------QUESTION 5--------------------------------")

alphabet={'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13,
'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25,
'.':26, ' ':27, ',':28, '!':29}
inv_alphabet={0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G',7: 'H',8: 'I',9: 'J',10: 'K',11: 'L',12: 'M',13: 'N',14:
'O',15: 'P',16: 'Q', 17:'R',18: 'S',19: 'T',20: 'U',21: 'V',22: 'W',23: 'X',24: 'Y',25: 'Z',26:
'.',27: ' ',28: ',',29: '!'}
def egcd1(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd
listSol={}
def posSol():
    for a in alphaList:
        for b in range(900):
            if (a*803+b)%900== 562:
                gamma = modinv(a, 900)
                theta = 900-(gamma*b)%900
                listSol[gamma]=theta


def encodeCipher(ctext,g,b):
    ptext=''
    clen=len(ctext)
    x=0
    for i in range(clen//2):
        f=ctext[x]
        s=ctext[x+1]
        encode= alphabet[f]*30 + alphabet[s]
        poz= (encode*g+b)%900
        pozf=poz//30
        pozs=poz%30
        ptext+=inv_alphabet[pozf]
        ptext+=inv_alphabet[pozs]
        x=x+2

        
    return ptext


    
ctext="ZHOFC.BNZCLRZ WNJ.XGI.WMBDV.MEJ!GGYKGDZ ERGMWNJ.KDGD RSW"

alphaList=[]
def possibleAlpha(x):
    for a in range(x):
        gcd=egcd1(a,x)
        if gcd==1:
            alphaList.append(a)
possibleAlpha(900)
posSol()
print("Possibble gamma, theta pairs that SW will point to .X are: ")
for gamma, theta in listSol.items():
    ptext=encodeCipher(ctext,gamma,theta)
    print("Gamma=", gamma, "Theta= ", theta ," ptext= ", ptext)

print("Solution found!! With decryption key Gamma= 811 Beta= 421 the ptext is SING, GODDESS, OF THE ANGER OF ACHILLES, SON OF PELEUS.")
"""









