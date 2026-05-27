k = 9
a= [2,7,11,15]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==k:
            print(i,j)