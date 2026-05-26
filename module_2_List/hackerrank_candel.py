#candel question


a= [44,53,31,27,77,60,66,77,26,36]
b= max(a)
print(b)
c=0
for i in range(len(a)):
    if a[i]==b:
        c= c+1
print(c)