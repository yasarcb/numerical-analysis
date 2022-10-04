from math import *

print("üstel fonksiyonlar için ** ifadesini kullanınız")
print("verdiğiniz açı degerlerini radyan cinsinden yazınız ( 1 derece = pi/180 radyan )")
print(" ln() ifadesi yerine log() ifadesini kullanınız")
e=2.71
x = float(input("x degerini giriniz:"))
f = eval(input("f(x) fonksiyonun degerini giriniz :"))
ftürev = eval(input("f(x) fonksiyonun türevini giriniz:"))

eps = float(input("epsülon degerini giriniz:"))

s=1
while (s > eps):
    x1=0
    x1 = x - (f / ftürev)
    print("bir sonraki x degeri:{}".format(x1))
    x = float(input("x degerini giriniz:"))
    f = eval(input("f(x) fonksiyonun degerini giriniz :"))
    s= abs(x-x1)