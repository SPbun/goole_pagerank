# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pylab as plt
import operator

#load the relation_matrix
relation_matrix = np.loadtxt("result_matrix.txt")

#init the x[] and y[]
x = list(np.zeros((1)))
y = list(np.zeros((1)))

for i in range(0,500):
    for j in range(0,500):
        if relation_matrix[i][j] == 1:
            x.append(i)
            y.append(j)
            
 
# plot the x[],y[]
plt.scatter(x,y,s = 1)
plt.show()

#init the matrix L
L = np.zeros((500,500))
for i in range(0,len(x)):
    L[int(x[i])][int(y[i])] = 1

#translate L into A
for i in range(0,500):
    sum = 0
    for j in L[:,i]:
        sum += j
    if not  sum == 0:
        L[:,i] = L[:,i]/sum
A = L

A = np.array(A)
#power iteration for G
X = np.zeros((500,1))
#init a random vector
X[0][0] = 1
# init e and k
e = np.ones((500,1))
k = 0.85

for i in range(0,5000):
    Y = np.dot(A,X)

    B = 1 - k*np.sum(Y)
    X = k*Y + (B/500)*e
# V is the result
V = X

#load the urls from file 
f = open('result__www.scutde.net.txt','r')
urls = []
while True:
    url = f.readline().rstrip('\n')
    if url:
        urls.append(url)
    else:
        break

#generate a dictionary that has a map from url to vector V
V_dic = {}
V = list(V)
for i in range(0,500):
    V_dic[urls[i]] = float(V[i])

#sort the V_dic by its values 
sorted_result=sorted(V_dic.items(),key=operator.itemgetter(1),reverse=True)
#output the top 20 results
for i in range(0,20):
    print('{} : {}'.format(i+1,sorted_result[i][0]))