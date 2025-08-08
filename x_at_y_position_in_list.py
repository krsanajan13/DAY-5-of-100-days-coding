l1=[10,20,30,40,50]
index=2
element=60
l1+=[0]
for i in range(len(l1)-2,index-1,-1):
    l1[i+1]=l1[i]
l1[index] = element

print(l1)