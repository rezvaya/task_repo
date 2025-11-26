"""
Постройте график параболы y=x^2 для x от -10 до 10. Добавьте заголовок, подписи осей и сетку.
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 200)
y = x ** 2

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()