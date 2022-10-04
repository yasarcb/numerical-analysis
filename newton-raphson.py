from math import *



print("**********************************************************************************")
print("*üstel fonksiyonlar için ** ifadesini kullanınız                                 *")
print("*verdiğiniz açı degerlerini radyan cinsinden yazınız ( 1 derece = pi/180 radyan) *")
print("*ln() ifadesi yerine log() ifadesini kullanınız                                  *")
print("**********************************************************************************")
print("  ")


eps = float(input("epsülon degerini giriniz:"))

s=1

while(s > eps):
    x = float(input("x degerini giriniz:"))
    f = eval(input("f(x) fonksiyonun degerini giriniz :"))
    ftürev = eval(input("f(x) fonksiyonun türevini giriniz:"))
    x1 = 0
    x1 = x - (f/ftürev)
    s= abs(x-x1)
    print("bir sonraki x degeri:{}".format(x1))

