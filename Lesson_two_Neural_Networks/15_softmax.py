# Lesson 2 Part 15 on the softmax function

import numpy as np

def softmax(L):
    output = []
    for i in range(len(L)):
        val = np.exp(L[i]) / np.sum(np.exp(L[:]))
        output.append(val)

    return output

""" 
alternatives:

expL = np.exp(L)
sumExpL = sum(expL)
result = []
for i in expL:
    result.append(i * 1.0/sumExpL)
return result

or 

expL = np.exp(L)
return np.divide(expL, expL.sum())
"""

if __name__ == "__main__":
    L = [5, 6, 7]
    sftmx = softmax(L)
    print(sftmx)
