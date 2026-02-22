list=[3,9,5,2]
max=list[0]
for i in range(1,len(list)):
    if list[i]>max:
        max=list[i]
print(max)