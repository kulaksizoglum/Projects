

import random
import requests
#import BitVector
import numpy as np 

API_URL = 'http://harpoon1.sabanciuniv.edu:9999'
my_id = 25368
def get_poly():
  endpoint = '{}/{}/{}'.format(API_URL, "poly", my_id )
  response = requests.get(endpoint) 	
  a = 0
  b = 0
  if response.ok:	
    res = response.json()
    print(res)
    return res['a'], res['b']
  else:
    print(response.json())

def check_mult(c):
  #check result of part a
  endpoint = '{}/{}/{}/{}'.format(API_URL, "mult", my_id, c)
  response = requests.put(endpoint) 	
  print(response.json())

def check_inv(a_inv):
  #check result of part b
  response = requests.put('{}/{}/{}/{}'.format(API_URL, "inv", my_id, a_inv)) 
  print(response.json())

a, b = get_poly()
##SOLUTION  
a_order=[]
b_order=[]
 
p_x= [1,1,1,0,0,0,0,1,1] 

for i in range(len(a)):
  if a[i]=="1":
    a_order.append(1)
  else:
    a_order.append(0)
  
for i in range(len(b)):
  if b[i]=="1":
    b_order.append(1)
  else:
    b_order.append(0)

def multiplyfunc(s1,s2):
  sol=""
  res = [0]*(len(s1)+len(s2)-1)

  for o1,i1 in enumerate(s1):
      for o2,i2 in enumerate(s2):
          res[o1+o2] += i1*i2
  quotient, remainder = np.polydiv(res, p_x)
  #print("\n\nquotient  : ", quotient) 
  #print ("\n")
  for i in remainder:
    if i%2==0:
      sol+="0"
    else:
      sol+="1"
  print("a(x)xb(x)is in gf(2^8)is ",sol)
  check_mult(sol)

def inversefunc(array,s1,p_x):
  res = [0]*(len(array)+len(s1)-1)
  sol=""
  for o1,i1 in enumerate(array):
      for o2,i2 in enumerate(s1):
          res[o1+o2] += i1*i2
  quotient, remainder = np.polydiv(res, p_x)
  for i in remainder:
    if i%2==0:
      sol+="0"
    else:
      sol+="1"
  if sol=="00000001":
    print(array)
    res=""
    for i in array:
      res+=str(i)
    print("Multiplicative inverse of a(x)is",res )

    check_inv(res)

multiplyfunc(a_order,b_order)

result_array = np.unpackbits(np.arange(256, dtype=np.uint8).reshape(-1, 1), axis=1)
for i in result_array:
  inversefunc(i,a_order,p_x)















