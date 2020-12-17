'''
filter 사용하기

'''
import numpy as numpy

arr = numpy.array([5,8,9,6,3])

filter = numpy.where(arr > 5)
print(arr[filter])
