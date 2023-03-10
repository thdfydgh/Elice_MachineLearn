import numpy as np
import pandas as pd

#------------------------------------------------------------------------------------#
#Series Data!
# 두 개의 시리즈 데이터가 있다.

print("Population series data:")
population_dict = {
    'korea': 5180,
    'japan': 12718,
    'china': 141500,
    'usa': 32676
}
population = pd.Series(population_dict)
print(population, "\n")

print("GDP series data:")
gdp_dict = {
    'korea': 169320000,
    'japan': 516700000,
    'china': 1409250000,
    'usa': 2041280000,
}
gdp = pd.Series(gdp_dict)
print(gdp, "\n")


# 이곳에서 2개의 시리즈 값이 들어간 데이터프레임을 생성한다.
print("Country DataFrame")
country = pd.DataFrame({
    
    'population' : population,
    'gdp' : gdp
    
})

print(country)
print(country.index)
print(country.columns)

#------------------------------------------------------------------------------------#
print("#------------------------------------------------------------------------------------#")
# 마스킹 & queryfunction
#------------------------------------------------------------------------------------#

print("Masking & query")
df = pd.DataFrame(np.random.rand(5, 2), columns=["A", "B"])
print(df, "\n")

# 데이터 프레임에서 A컬럼값이 0.5보다 작고 B컬럼 값이 0.3보다 큰값들을 구해봅시다.
# 마스킹 연산을 활용하여 출력!
print(df[(df['A']<0.5) &( df['B'] > 0.3) ])

# query 함수를 활용하여 출력!

print(df.query("A < 0.5 and B > 0.3"))






