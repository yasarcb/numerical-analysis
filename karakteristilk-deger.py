import numpy as np

n = int(input("n sayisini giriniz: "))

print("katsayi matrisinin ")
matris = np.array([[float(input(f'{i + 1}.satirin  {j + 1}. sutununu giriniz: ')) for j in range(n)] for i in range(n)])
print("matris:")
print(matris)

ters_matris = np.linalg.inv(matris)

print("ters matris:")
print(ters_matris)
print("")

print("başlangıç matrisinin ")
v = np.array([[float(input(f'{i + 1}.satiri giriniz: '))] for i in range(n)])
print(v)

alfa_k = np.zeros([n,1])
alfa= np.zeros([n,1])

vv=np.zeros([n,1])
vvv =np.zeros([n,1])

vvv=v


w = 0
iterasyon = int(input("iterasyon degerini giriniz:"))

while (w < iterasyon):

    for i in range(0, n):
        alfa_k[i] = 0
        alfa[i] = 0
        for j in range(0, n):
            alfa_k[i] += np.array(ters_matris[i][j] * v[j])
            alfa[i] += np.array(matris[i][j] * vvv[j])

    q = max(alfa_k)
    qb = max(alfa)

    vv = np.array(alfa_k / q)
    v = vv

    vvb = np.array(alfa / qb)
    vvv = vvb

    w = w + 1

print("en küçük deger:")
q = 1 / q
print(q)




print("en büyük deger:")
print(qb)

