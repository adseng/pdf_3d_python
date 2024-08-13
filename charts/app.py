import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('x')
plt.title('Sin Function')
# 保存为图片, 保存到项目下的 out文件夹
plt.savefig('sin.png')