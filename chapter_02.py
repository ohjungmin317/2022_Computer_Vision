import numpy as np

# 배열의 모든 요소가 같은 타입이어야 한다.
# 타입이 일치하지 않을 경우 가능한 상위 타입을 취한다.

# (1)
# arr = {1,4,2,5,3}
# n_arr = np.array(arr)

# (2)
# arr = {'3.14', 2., 5, 3}
# n_arr = np.array(arr)

# (3)
# arr = {'3.14', 2., 5, 3}
# n_arr = np.array(arr,dtype='float64')
#
# print(arr)
# print(type(arr))
# print(n_arr)
# print(type(n_arr))

# nums = np.array([1,4,2,5,3])

# print(nums)
# print(nums.ndim)
# print(nums.shape)
# print(len(nums.shape))
# print(nums.size)

# numpy slice 하는 법
# print(nums[1])
# print(nums[:3])
# print(nums[2:4])
# print(nums[::2])


nums = np.array([[1,4,2],[7,5,3]])

# print(nums)
# print(nums.ndim)
# print(nums.shape) # ( 행렬 2 * 3 )
# print(len(nums.shape))
# print(nums.size)

# print(nums)
# print(nums[0,2])
# print(nums[0][2])

# print(nums)
# print(nums[0:1, ])
# print(nums[0:1,:])
# print(nums[:,1:2])
# print(nums[1,1:])
# print(nums[0:,1:])

# 실습
print(nums)
print(nums[1,1])
print(nums[1,0:2])
print(nums[:,2:3])
print(nums[:,0:2])



