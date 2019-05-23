import numpy as np

a = np.array( [ [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]] )

b = np.array( [ [9, 8, 7],
                [6, 5, 4],
                [3, 2, 1]] )

c = np.array([a, b])

print(a.shape)
print(b.shape)
print(c.shape)
print(np.mean(c, axis=0))
# (3, 3)
# (3, 3)
# (2, 3, 3)
# [[5. 5. 5.]
#  [5. 5. 5.]
#  [5. 5. 5.]]