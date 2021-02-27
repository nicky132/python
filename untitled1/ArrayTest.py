import numpy as np
arr = np.array([
    [0,1,2,3,4,5,6,7,8,9,10,11],
    [12,13,14,15,16,17,18,19,20,21,22,23]
])
print('数组的维数',arr.ndim)
print('数组元素的总个数',arr.size)
print('数组中的元素在内存中所占的字节数',arr.itemsize)
print('整个数组所占的存储空间',arr.nbytes)
print('整个数组所占的存储空间',arr.size*arr.itemsize)
print('整个数组所占的存储空间',arr.size*arr.itemsize)
print('整个数组所占的存储空间',arr.size*arr.itemsize)
arr.resize(6,4)
print(arr)
print('转置后')
print(arr.T)
print('实现复数办法：')
arr2 = np.array([1.j+1,2.j+3])
print('复数数组的实部')
print(arr2.real)
print('复数数组的虚部')
print(arr2.imag)

# flat
arr3 = np.arange(4).reshape(2,2)
print(arr3)
f = arr3.flat
print('flat用法')
for item in f:
    print(item)
# 访问第二个元素
f[2] = 20
print('可用索引访问',f[2])
# print(f[0])