import numpy as np

n = int(input("n sayisini giriniz: "))


x=np.zeros([n,1])
x1=np.zeros([n,1])
b1=np.zeros([n,1])
matris3=np.zeros([n,n])

print("katsayi matrisinin ")
matris = np.array([[float(input(f'{i + 1}.satirin  {j + 1}. sutununu giriniz: ')) for j in range(n)] for i in range(n)])
print(matris)

print("cozum matrisinin ")
b = np.array([[float(input(f'{i + 1}.satiri giriniz: '))] for i in range(n)])
print(b)

print("x matrisinin ")
x1 = np.array([[float(input(f'{i + 1}.satiri giriniz: '))] for i in range(n)])
print(x1)

for i in range(0, n):
    if (abs(matris[i][0]) > abs(matris[i][1]) and abs(matris[i][0]) > abs(matris[i][2])):
        matris3[0][0] = matris[i][0]
        matris3[0][1] = matris[i][1]
        matris3[0][2] = matris[i][2]
        b1[0] = b[i]
    elif (abs(matris[i][1]) > abs(matris[i][0]) and abs(matris[i][1]) > abs(matris[i][2])):
        matris3[1][0] = matris[i][0]
        matris3[1][1] = matris[i][1]
        matris3[1][2] = matris[i][2]
        b1[1] = b[i]
    elif (abs(matris[i][2]) > abs(matris[i][0]) and abs(matris[i][2]) > abs(matris[i][1])):
        matris3[2][0] = matris[i][0]
        matris3[2][1] = matris[i][1]
        matris3[2][2] = matris[i][2]
        b1[2] = b[i]

print(matris3)
print(b1)


a = 0
w=int(input("iterasyon sayısını giriniz:"))
q=1

while(q<w+1):
    for i in range(0,n):
        a = 0
        for j in range(0, n):
            if(i != j ):
                a +=np.array(matris3[i][j] * x1[j] )
        x[i]= np.array((b1[i] - a)/matris3[i][i])

    x1=x
    print("cevap matrisi:")
    print(x)
    q=q+1


