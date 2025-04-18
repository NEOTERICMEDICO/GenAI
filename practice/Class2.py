import matplotlib.pyplot as plt
import numpy as np

x = (-4.2, -3, -2.8, 0.5, 1, 1.6, 3.2, 6.4)
y = (-10.1, -6.1, -4.9, 6.2, 9.8, 12.1, 18.5, 30.8)

print(x)

plt.scatter(x, y, color='red', marker='o')
print(x, y)
plt.title('Scatter Plot') 