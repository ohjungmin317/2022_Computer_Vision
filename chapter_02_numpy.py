import numpy as np

# (1) Numpy 0차원 일때
# nums = np.array(3)
# print(nums)
# print(nums.ndim)
# print(nums.shape)

# (2) Numpy 3차원 배열
# nums = np.array([1,4,2,5,3])
# ref = nums[1:4]
# cpy = nums[1:4].copy() # copy를 사용하는 경우 독립적으로 사용이 되기 때문에 값에 영향을 받지 않는다.
# print(ref)
# print(cpy)
# nums[2] = 10 # 참조되는 경우 값이 변경이 되서 나오게 된다.
# print(ref)
# print(cpy)

# (3) Numpy 내장 함수 사용
# print(np.zeros((2,2)))
# print(np.ones((1,2)))
# print(np.full((2,2), 7))
# print(np.random.random((2,2)))
# print(np.linspace(0,1,num=5, endpoint=True))
# print(np.arange(1,5,1))

# (4) 행열 전환과 형태 변형
# num = np.array([1,2,3,4,5,6,7,8,9])
# num_reshape = num.reshape(9,1) # 아이템 수가 같아야 한다. item이 9개 이기 때문에 3*3 행렬이 가능하다.
# print(num_reshape)
# num_T = num_reshape.T
# print(num_T) # == axis_1 / axis_2 서로 축을 바꾸면 된다.

# (5) Numpy 배열 연결
# x = np.array([1,2,3])
# y = np.array([4,5,6])
# z = np.array([[1,2,3],
#              [4,5,6]])
# print(np.concatenate([x,y]))
# print(np.concatenate([z,z]))
# print(np.concatenate([z,z], axis=1)) # default = 0 행을 기준으로
# print('---------------------')
# print(np.vstack([x,y])) # axis = 0
# print('---------------------')
# print(np.hstack([x,y])) # axis = 1

# (6) Numpy 배열의 분할
# num = [1,2,3,4,5,6,7,8,9]
# x1,x2,x3 = np.split(num, [2,5])
# print(x1,x2,x3)
# print('---------------------')
# grid = np.arange(9).reshape(3,3)
# print(grid)
# print('---------------------')
# upper , lower = np.split(grid,[2])
# print(upper)
# print('---------------------')
# print(lower)
# print('---------------------')
# right , left = np.split(grid,[2],axis=1)
# print(right)
# print('---------------------')
# print(left)

# (7) Numpy 배열의 연산
# arr = [100,80,70,90,110]
# narr = np.array(arr)
# print((narr-32) * 5 / 9)

# (8) 브로드 캐스팅 : 연산 대상인 두 배열들의 차원이 같은 경우 각 요소 단위로 연산을 수행
a = np.arange(1,5) #[0,1,2,3,4]
b = np.array(3) #[3,3,3]
print(a+b)