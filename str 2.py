__author__ = 'student'
import random
random.seed(0)
N=int(input())
S=0
for n in range (1,N):
    u=random.uniform(-3,3)
    if u >= -2 and u <=2:
        y=-u**2+4
    else:
        y=0
    S+=y
S=6*S/N
print(S)
