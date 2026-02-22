list=[1,2,3,4,5,6,7,8,9]
min=list[0]
for j in range(1,len(list)):
    if list[j]<min:
        min=list[j]
print(min)