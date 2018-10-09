import numpy as np
"""
no_shift = np.array(   [[  26.4, 2772. ],
                            [  28.2, 2397. ],
                            [  30. , 2550. ],
                            [  31.8, 2703. ],
                            [  33.6, 2856. ]])
    # Note that for all readings above have the same ratio. Below we construct
    # input with a gear shift.
exam = np.empty(no_shift.shape[0],no_shift.dtype)
for i in range(no_shift.shape[0]):
    exam[i] = np.divide(no_shift[i,1],no_shift[i,0])
print(exam)
str = False
for i in range(exam.shape[0]):
    if(i+1 >= exam.shape[0]):
        break
    print(abs(exam[i]-exam[i+1]))
    if(abs(exam[i]-exam[i+1]) >= 10):
        str = True
print(str)
"""
y = np.eye(5)[::-1]
print(y)