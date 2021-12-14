import numpy as np
# 2021-12-14 Tue ~ 2021-12-15
# 한글 폰트 깨지는 결과물
from matplotlib import pyplot as plt

np.random.seed(0)

x = range(7)
y = 10 + 5 * np.random.randn(7)
fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_title('한글 지정 타이틀')
ax.bar(x, y)
plt.show()


