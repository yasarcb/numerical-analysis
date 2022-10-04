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
    c1 = float(math.gamma(s) / (math.gamma(s - 1) * math.gamma(1)))
    c2 = float(math.gamma(s) / (math.gamma(s - 2) * math.gamma(2)))
    c3 = float(math.gamma(s) / (math.gamma(s - 3) * math.gamma(3)))
    c4 = float(math.gamma(s) / (math.gamma(s - 4) * math.gamma(4)))

    s1 = c1 * delta[0]
    s2 = c2 * delta1[0]
    s3 = c3 * delta2[0]
    s4 = c4 * delta3[0]

    s5 = fonk[0]
    sonuc = s1 + s2 + s3 + s5 +s4
else:
    h = x[1] - x[0]
    s = (y - x[4]) / h
    c1 = float(math.gamma(s) / (math.gamma(s - 1) * math.gamma(1)))
    c2 = float(math.gamma(s) / (math.gamma(s - 2) * math.gamma(2)))
    c3 = float(math.gamma(s) / (math.gamma(s - 3) * math.gamma(3)))
    c4 = float(math.gamma(s) / (math.gamma(s - 4) * math.gamma(4)))

    s1 = c1 * delta[3]
    s2 = c2 * delta1[2]
    s3 = c3 * delta2[1]
    s4 = c4 * delta3[0]
    s5 = fonk[4]
    sonuc = s1 + s2 + s3 + s4 + s5
print(sonuc)
