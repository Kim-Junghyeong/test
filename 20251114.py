# Numpy 실습
# 실습1

# 1

import numpy as np

a = np.zeros((3,4))

b = np.full(a.shape,5)

print(f"문제1 : {b}")

# 2

import numpy as np

a = np.arange(0,20,2)

print(f"문제 2: {a}")

# 3

import numpy as np

a = np.random.rand(2,3)

print(f"문제3 : {a}")

# 4

from numpy.random import default_rng

rng = default_rng(seed=42)

a = rng.normal(100, 20, size = 6)

print(a)


# 실습 2. 인덱싱과 슬라이싱(1)

# 1. 다음 배열에서 2, 4, 6번째 요소를 Fancy Indexing으로 선택
import numpy as np

arr = np.arange(10,30,2)
print(arr[[1, 3, 5]])

# 3. 3x4배열에서 마지막 열만 선택해 모두 -1로 변경하시오.

import numpy as np

arr = np.arange(1,13).reshape(3,4)
print(arr)

arr[0:3,3:] = -1
print(arr)


# 실습3

# 2. 0~99 난수 (10,10) 배열 생성 후, 짝수 인덱스 행만 출력

from numpy.random import default_rng

rng = default_rng(seed=42)

a = rng.integers(1,99,size =(10,10))

print(a[1::2,:])

# Numpy(2)

# 실습1. 배열 연산(1)

# 1. 배열 생성 후 모든 요소에 3을 더하시오.

import numpy as np

arr = np.array([1, 2, 3, 4])

a = 3

print(arr + a)

# 2. 2차원 배열에서 각 요소를 -1로 곱한 새로운 배열
import numpy as np

arr = np.array([[5, 10],
                [15, 20]])

arr2 = arr * -1

print(arr2)

# 3. 두 배열의 곱셈과 나눗셈
import numpy as np

arr1 = np.array([2, 4, 6])
arr2 = np.array([1, 2, 3])

print(arr1 * arr2)
print(arr1 / arr2)


# 실습2. 통계함수 및 집계연산(2)

# 1. 아래 배열에서 전체 합계과 평균을 각각 구하세요.

import numpy as np

arr = np.array([5, 10, 15, 20])

print(np.sum(arr))
print(np.mean(arr))


# 4. 아래 배열에서 행별 평균과 열별 평균을 각각 구하세요.

import numpy as np

arr = np.array([[10,20],
                [30, 40],
                [50, 60]])

print(np.mean(arr, axis=0))
print(np.mean(arr, axis=1))

# 실습4. 행렬 곱셈

# 2. 4x4단위행렬 I와 4x4 난수행렬 M(0~9사이 정수) 간의 곱을 구하고

import numpy as np
from numpy.random import default_rng

rng = default_rng(seed=42)

I = np.eye(4,4)
M = rng.integers(0,9,size=(4,4))

print(M)
print("--------------")
print(M@I)

# 3. 모든 값이 1인 (2,5) 배열 X와 5부터 14까지 연속된 정수로 채워진 (5,2) 배열 Y 곱

import numpy as np

X = np.ones((2,5))
Y = np.arange(5,15).reshape(5,2)

print(X@Y)

# Numpy(3)

# 실습1. 배열 형태 변형, 차원 확장, 축소

# 1
# 1) ravel과 flatten을 각각 사용해 1차원 배열로 변환하고,
# 2) arr의 첫 번째 원소(arr[0,0])를 999로 바꾼 뒤 ravel 결과와 flatten 결과 보기
import numpy as np

arr = np.array([[10,20],[30,40],[50,60]])

arr1 = arr.ravel()
print(arr1)
print("-------")
arr2 = arr.flatten()
print(arr2)
print("-------")
arr[0,0] = 999

print(arr1)
print("-------")
print(arr2)

# 2 크기 32 x 32인 이미지 데이터를 가정하고, 이 배열에 대해
# expand_dims를 사용하여 shape (1, 32, 32)로 바꾸는 코드를 작성하시오

import numpy as np

img = np.random.rand(32,32)
print(img.shape)
print("--------")
img1 = np.expand_dims(img, axis=0)
print(img1.shape)
print("--------")