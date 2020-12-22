import math as mt
import matplotlib.pyplot as plt
import numpy as np

m = 1
n = 1001

r = []
nm = []
mn = []
n_m = []

def pr_fp(m, n):
    k = mt.ceil(m * mt.log(2)/n)
    return mt.pow((1 - mt.pow((1 - 1/m),(k*n))),k)

for i in range(10):
    a = pr_fp(m, n)
    r.append(a)
    nm.append(n/m)
    mn.append(m/n)
    n_m.append(n - m)
    m += 100
    n -= 100

a = pr_fp(m, n)
r.append(a)
nm.append(n/m)
mn.append(m/n)
n_m.append(n - m)
print(n_m)
print(n)
print(m)
#print(n/m)
#print(r)
#print(nm)



 
# RESULTADOS PARA |v|=100

#categoria = ['n/m', 'Fibonacci con ρ=0.2', 'Binary con ρ=0.8', 'Fibonacci con ρ=0.8']
#Definimos una lista con ventas como entero

#tiempos1 = [0.003225899999999997, 0.006413233333333333, 0.006307566666666667, 0.012006733333333333]
 
fig, ax = plt.subplots()
#Colocamos una etiqueta en el eje Y
ax.set_ylabel('Probabilidad')
ax.set_xlabel('n - m')
#Colocamos una etiqueta en el eje X
ax.set_title('Probabilidad de Falso Positivo v/s  n-m')
#Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
#plt.bar(mn, r)
plt.plot(n_m, r, color="green", linewidth=1.0, linestyle="-")
plt.savefig('resultsP8.png')
#Finalmente mostramos la grafica con el metodo show()
plt.show()