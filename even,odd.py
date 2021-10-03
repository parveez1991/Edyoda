import numpy as np
numbers= np.array([[1,2,3],[4,5,6],[7,8,9]])

odd = numbers[numbers%2 == 1].size
even = numbers[numbers%2 == 0].size

print(odd, even)