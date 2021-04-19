import numpy as np
from scipy.stats import binom

f = open("Lab 1 Data.txt", "r")
D = np.array

for char in f.read() :
    if char.isdigit():
        D = np.append(D, int(char))

f.close()
D = np.reshape(D[1::], (60, 200))

# Idea: A human pretending to be random will follow certain pattern3 more often than a random number generator

# For distribution of 0:s and 1:s
mean1 = 100
sums = np.sum(D, 1)
sumsDeviations = np.zeros(60, int)

# All possible patterns of two digits
pattern2 = np.array([[0, 0], [1, 0], [0, 1], [1, 1]]) 
pattern2Cnt = np.zeros((60, 4), int)
pattern2Deviations = np.zeros(60, int)

# All possible patterns of three digits
pattern3 = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1]]) 
pattern3Cnt = np.zeros((60, 8), int)
pattern3Deviations = np.zeros(60, int)

# All possible patterns of four digits
pattern4 = np.array([[0, 0, 0, 0], [1, 1, 1, 1],        
                     [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1],
                     [1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 0, 1], [0, 0, 1, 1],
                     [1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]])
pattern4Cnt = np.zeros((60, 16), int)
pattern4Deviations = np.zeros(60, int)

# Standard deviation of binomial distribution
n1 = 200
n2 = 199
n3 = 198
n4 = 197

p1 = 1/2
p2 = 1/4
p3 = 1/8
p4 = 1/16

std1 = binom.std(n1, p1)
std2 = binom.std(n2, p2)
std3 = binom.std(n3, p3)
std4 = binom.std(n4, p4)

# Count number of patterns
nStd = 2
for i in range(np.size(D, 0)) :

    if sums[i] < mean1 - nStd*std1 or sums[i] > mean1 + nStd*std1 :
        sumsDeviations[i] += 1

    for j in range(np.size(D, 1)-1) :

        for k in range(np.size(pattern2, 0)) :
            if D[i,j] == pattern2[k,0] and D[i,j+1] == pattern2[k,1] :
                pattern2Cnt[i,k] += 1

        for k in range(np.size(pattern3, 0)) :
            if j < np.size(D, 1)-2 and D[i,j] == pattern3[k,0] and D[i,j+1] == pattern3[k,1] and D[i,j+2] == pattern3[k,2] :
                pattern3Cnt[i,k] += 1
        
        for k in range(np.size(pattern4, 0)) :
            if j < np.size(D, 1)-3 and D[i,j] == pattern4[k,0] and D[i,j+1] == pattern4[k,1] and D[i,j+2] == pattern4[k,2] and D[i,j+3] == pattern4[k,3] :
                pattern4Cnt[i,k] += 1
    
    # Calculate number of patterns that differ with more than 2 standard deviations for each row
    mean2 = np.mean(pattern2Cnt[i,:])
    for v in pattern2Cnt[i,:] :
        if v < mean2 - nStd*std2 or v > mean2 + nStd*std2 :
            pattern2Deviations[i] += 1

    mean3 = np.mean(pattern3Cnt[i,:])
    for v in pattern3Cnt[i,:] :
        if v < mean3 - nStd*std3 or v > mean3 + nStd*std3 :
            pattern3Deviations[i] += 1

    mean4 = np.mean(pattern4Cnt[i,:])
    for v in pattern4Cnt[i,:] :
        if v < mean4 - nStd*std4 or v > mean4 + nStd*std4 :
            pattern4Deviations[i] += 1

# Printing data that I added to a tables in the report
print(mean1, mean2, mean3, mean4)
print(std1, std2, std3, std4)

print(sums)
print(pattern2Cnt)
print(pattern3Cnt)
print(pattern4Cnt)

print(sumsDeviations)
print(pattern2Deviations)
print(pattern3Deviations)
print(pattern4Deviations)

print(np.array(np.nonzero(sumsDeviations))+1)
print(np.array(np.nonzero(pattern2Deviations))+1)
print(np.array(np.nonzero(pattern3Deviations))+1)
print(np.array(np.nonzero(pattern4Deviations))+1)

for i, x in enumerate(pattern3Deviations):
    if x > 1:
        print(i+1)

for i, x in enumerate(pattern4Deviations):
    if x > 1:
        print(i+1)
