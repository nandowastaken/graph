import matplotlib.pyplot as plt

def afim(x, a, b):
    return a * x + b

def quadratica(x, a, b, c):
    return a * x ** 2 + b * x + c

x = [1,2,3, 4, 5, 6, 7, 8, 9]
y = [afim(i, 2, 1) for i in x]
plt.plot(x, y, label = "afim")

y2 = [quadratica(i, 1, 2, 1) for i in x]
plt.plot(x, y2, label = "quadratica")


plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('My first graph!')

plt.show()
