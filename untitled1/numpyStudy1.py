# coding:utf-8
import numpy as np
arr = np.array([[0,1,2],
               [3,4,5],
               [6,7,8]])
print(arr)
result1 = np.split(arr,3,axis=1)
print(result1[0])
print(result1[1])
print(result1[2])

print('利用np.hsplit水平分割数组')
result2 = np.hsplit(arr,3)
print(arr)
print(result2[0])
print(result2[1])
print(result2[2])

print('利用np.split垂直分割数组')
result3 = np.split(arr,3,axis=0)
print(arr)
print(result3[0])
print(result3[1])
print(result3[2])

print('按深度方向分割数组')
arr1 = np.arange(8).reshape(2,2,2)
print(arr1)
result5 = np.dsplit(arr1,2)
print(result5[0])
print(result5[1])