import numpy as np

# 배열의 기초!

#------------------------------------------------------------------------------------#

print("1차원 array")
array = np.array(range(10))
print(array)

# 1. array의 자료형을 출력
print(type(array))
# 2. array의 차원을 출력
print(array.ndim)
# 3. array의 모양을 출력
print(array.shape)
# 4. array의 크기를 출력
print(array.size)
# 5. array의 dtype(data type)을 출력
print(array.dtype)
# 6. array의 인덱스 5의 요소를 출력
print(array[5])
# 7. array의 인덱스 3의 요소부터 인덱스 5 요소까지 출력
print(array[3:6])

print("#------------------------------------------------------------------------------------#")

#------------------------------------------------------------------------------------#

print("2차원 array")
#1부터 15까지 들어있는 (3,5)짜리 배열을 만듭니다.
matrix = np.array(range(1,16))
matrix.shape = 3,5
print(matrix)

# 1. matrix의 자료형을 출력
print(type(matrix))
# 2. matrix의 차원을 출력
print(matrix.ndim)
# 3. matrix의 모양을 출력
print(matrix.shape)
# 4. matrix의 크기를 출력
print(matrix.size)
# 5. matrix의 dtype(data type)을 출력
print(matrix.dtype)
# 6. matrix의 dtype을 str로 변경하여 출력
print(matrix.astype('str'))
# 7. matrix의 (2,3) 인덱스의 요소를 출력
print(matrix[2,3])
# 8. matrix의 행은 인덱스 0부터 인덱스 1까지, 열은 인덱스 1부터 인덱스 3까지 출력
print(matrix[0:2,1:4])
print("#------------------------------------------------------------------------------------#")
#Indexing & Slicing 
print("#Indexing & Slicing ")
#------------------------------------------------------------------------------------#

matrix2 = np.arange(1, 13, 1).reshape(3, 4)
print(matrix2)

# 1. Indexing을 통해 값 2를 출력
answer1 =  matrix2[0,1]

# 2. Slicing을 통해 매트릭스 일부인 9, 10을 가져와 출력
answer2 = matrix2[2:,:2]

# 3. Boolean indexing을 통해 5보다 작은 수를 찾아 출력
answer3 = matrix2[matrix2<5]

# 4. Fancy indexing을 통해 두 번째 행만 추출하여 출력
answer4 = matrix2[[1]]

print(answer1)
print(answer2)
print(answer3)
print(answer4)
#------------------------------------------------------------------------------------#

