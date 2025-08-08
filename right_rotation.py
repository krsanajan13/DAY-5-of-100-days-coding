l1=[10,20,30,40,50,60,70,80,90,100]
k=int(input())
k=k%len(l1)
rotated=l1[-k:]+l1[:-k]
print(rotated)