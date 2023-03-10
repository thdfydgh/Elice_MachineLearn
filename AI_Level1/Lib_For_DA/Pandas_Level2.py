import numpy as np
import pandas as pd

#--------------------------------------------------------------------------------------------#
    # 데이터프레임 값으로 정렬하기!

print("DataFrame: ")
df = pd.DataFrame({
    'col1' : [2, 1, 9, 8, 7, 4],
    'col2' : ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col3': [0, 1, 9, 4, 2, 3],
})
print(df, "\n")


# 정렬 코드 입력해보기    
# 1. col1을 기준으로 오름차순으로 정렬하기.
sorted_df1 = df.sort_values('col1', ascending = True)

# 2. col2를 기준으로 내림차순으로 정렬하기.
sorted_df2 = df.sort_values('col2', ascending = False)

# 3. col2를 기준으로 오름차순으로, col1를 기준으로 내림차순으로 정렬하기.
sorted_df3 = df.sort_values(['col2','col1'], ascending = [True, False])

#--------------------------------------------------------------------------------------------#

    #집계함수!

data = {
    'korean' : [50, 60, 70],
    'math' : [10, np.nan, 40]
}
df2 = pd.DataFrame(data, index = ['a','b','c'])
print(df2, "\n")

# 각 컬럼별 데이터 개수
col_num = df2.count(axis =0)
print(col_num, "\n")

# 각 행별 데이터 개수
row_num = df2.count(axis = 1)
print(row_num, "\n")

# 각 컬럼별 최댓값
col_max = df2.max()
print(col_max, "\n")

# 각 컬럼별 최솟값
col_min = df2.min()
print(col_min, "\n")

# 각 컬럼별 합계
col_sum = df2.sum()
print(col_sum, "\n")

# 컬럼의 최솟값으로 NaN값 대체
math_min = df2['math'].min()
df2['math'] = df2['math'].fillna(math_min)
print(df2, "\n")

# 각 컬럼별 평균
col_avg = df2.mean()
print(col_avg, "\n")
#--------------------------------------------------------------------------------------------#

    #그룹으로 묶기

df3 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'A', 'B', 'C'],
    'data1': [1, 2, 3, 1, 2, 3],
    'data2': [4, 4, 6, 0, 6, 1]
})
print("DataFrame:")
print(df3, "\n")

# groupby 함수를 이용
# key를 기준으로 묶어 합계를 구해 출력
print(df3.groupby('key').sum())

# key와 data1을 기준으로 묶어 합계를 구해 출력
print( df3.groupby(['key','data1']).sum() )

#--------------------------------------------------------------------------------------------#

df4 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'A', 'B', 'C'],
    'data1': [0, 1, 2, 3, 4, 5],
    'data2': [4, 4, 6, 0, 6, 1]
})
print("DataFrame:")
print(df4, "\n")

# aggregate를 이용하여 요약 통계량을 산출
# 데이터 프레임을 'key' 칼럼으로 묶고, data1과 data2 각각의 최솟값, 중앙값, 최댓값을 출력
print(df4.groupby('key').aggregate([min, np.median, max]))


# 데이터 프레임을 'key' 칼럼으로 묶고, data1의 최솟값, data2의 합계를 출력
print(df4.groupby('key').aggregate({'data1' : min, 'data2' : sum}))
