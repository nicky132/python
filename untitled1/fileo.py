arr1,arr2 = np.loadtxt('data.csv',delimiter=',',usecols=[6,7],unpack=True)
print(arr1)
print(arr2)
#加权平均价格
averageByWeight=np.average(arr1,weights=arr2)
print(averageByWeight)