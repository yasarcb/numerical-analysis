from math import *


print("üstel fonksiyonlar için ** ifadesini kullanınız")
print("verdiğiniz açı degerlerini radyan cinsinden yazınız ( 1 derece = pi/180 radyan )")
print(" ln() ifadesi yerine log() ifadesini kullanınız")
print("")

x=0
f = eval(input("f(x) fonksiyonun degerini giriniz :"))

eps = float(input("epsülon degerini giriniz:"))

s=1
a=12**x

while(s > eps):
    x = float(input("x{} degerini giriniz:".format(a)))
    x1 = float(input("x{} degerini giriniz:".format(a+1)))
    s = abs(x1-x)
    x2 = (x+x1)/2
    print("x{}. değer : {}".format(a+2,x2))
    a +=1
