# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "canillas"
__date__ = "$11 juin 2015 10:25:20$"
#from modinv import *
import random


def egcd(a,b):
    if a==0:
        return (b,0,1)
    else : 
        g,y,x=egcd(b%a,a)
        return(g , x-(b//a) * y , y)
    
def modiv(a,m):
    g,x,y = egcd(a,m)
    if g!= 1:
        raise Exeception ('Marche Pas')
    else:
        return x % m 

def GenN(p,q):
    return (p * q)

def GenPhiN(p,q):
    return((p-1)*(q-1))

def GenE(a):
  return(random.randint(1, a))

  
  
print("Hello")


a=313
b=167

print("P= Q= Secret")
print (a,b)

print("N=  Public")
print(GenN(a,b))

print("phiN=   Secret")
print(GenPhiN(a,b))

print("E=  Public")
e=281
print(e)

print("egcd=")
print(egcd(e,GenN(a,b)))

print('d= Secret')
print(modiv(e,GenPhiN(a,b)))
#je parle a
Message="USB"

#U=21
#S=19
#B=02

#blocks 
#211 902   M1 M2

#Chiffre 

#M1^clee public mod N
# C1 / C2

#output
#Source
#C1/C2
#Destinaitaire

eCam=61
nCam=9047
print("CAM ")
def ChiffrementCam(M1):
    return((M1**eCam)%nCam)
print(ChiffrementCam(211))
print(ChiffrementCam(902))


#dechiffrement 

#"C1" et "C2"

#C1**d%n

def DechiffrementCam(C1):
    return ((C1**17227)%24347)

print("CAM dechiffrement")
print(DechiffrementCam(12303))
print(DechiffrementCam(9054))

#signature 

#S=M1*d%n (clée privé)
#Mt=M1+S

#verification

#S**e%n