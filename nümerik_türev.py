import numpy as np
import math

n = int(input("kaç tane x sayısı girilecektir:"))

print("        x        ")
print("-----------------")
x = np.array([[float(input(f'{i + 1}.degeri: '))] for i in range(n)])


print("        f(x)  ")
print("-----------------")
fonk = np.array([[float(input(f'{i + 1}.degeri: '))] for i in range(n)])


y = float(input("x degerini giriniz:"))


delta = np.zeros([n,1])
delta1 = np.zeros([n-1,1])
delta2 = np.zeros([n-2,1])
delta3 = np.zeros([n-3,1])

for i in range(0, n - 1):
    delta[i] = np.array(fonk[i + 1] - fonk[i])

for i in range(0, n - 2):
    delta1[i] = np.array(delta[i + 1] - delta[i])

for i in range(0, n - 3):
    delta2[i] = np.array(delta1[i + 1] - delta1[i])

for i in range(0, n - 4):
    delta3[i] = np.array(delta2[i + 1] - delta2[i])

if (abs(y - x[0]) <= abs(y - x[n - 1])):
    h = x[1] - x[0]
    s = (y - x[0]) / h

    c2 = (2 * s - 1) / 2
    c3 = (3 * s ** 2 - 6 * s + 2) / 6
    c4 = (4 * s ** 3 - 18 * s ** 2 + 22 * s - 6) / 24

    s1 = delta[0]
    s2 = c2 * delta1[0]
    s3 = c3 * delta2[0]
    s4 = c4 * delta3[0]

    sonuc = (s2 + s3 + s1 + s4) / h
else:
    h = x[1] - x[0]
    s = (y - x[4]) / h

    c2 = (2 * s + 1) / 2
    c3 = (3 * s ** 2 + 6 * s + 2) / 6
    c4 = (4 * s ** 3 + 18 * s ** 2 + 22 * s + 6) / 24

    s1 = delta[2]
    s2 = c2 * delta1[1]
    s3 = c3 * delta2[0]
    s4 = c4 * delta3[0]

    sonuc = (s1 + s2 + s3 + s4) / h
print(sonuc)
