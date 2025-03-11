넘파이
넘파이 ndarray 개요

In [1]:
# 넘파이 모듈을 임포트
import numpy as np

In [2]:
array1 = np.([1, 2, 3])
print('array1 type:', type(array1))
print('array1 array 형태:', array1.shape)

array2 = np.array([[1, 2, 3],
                  [2, 3, 4]])
print('array2 type:', type(array2))
print('array2 array 형태:', array2.shape)

array3 = np.array([[1, 2, 3]])
print('array3 type:', type(array3))
print('array3 array 형태:', array3.shape)
