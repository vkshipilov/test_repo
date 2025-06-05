import numpy as np
import matplotlib.pyplot as plt

# Создаем массив значений x
x = np.linspace(-10, 10, 400)
# Вычисляем y = x^2
y = x ** 2

# Строим график
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Парабола: y = x^2')
plt.grid(True)
plt.show()
