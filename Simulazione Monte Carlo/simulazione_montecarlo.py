import numpy as np
import matplotlib.pyplot as plt

# Numeri dei punti della simulazione
n = 10

# Vettore coordinate punti casuali
x = np.random.rand(n)
y = np.random.rand(n)
Pi_greco = np.zeros(n)

# Vettore distanza
d = (x**2 + y**2)**(1/2)
print(d)

Ps = 0
Pq = 0
for i in range(n):
    Pq += 1
    if dist[i] < 1:
        Ps +=1

    Pi_greco[i] = 4*(Ps/Pq)

plt.figure(1)
plt.plot(Pi_greco)



