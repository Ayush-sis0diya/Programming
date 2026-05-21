'''
           3
           44
           555
           6666
           555
           44
           3
'''

n= 4
for i in range(1,n+1,1):
    y=i+2
    for j in range(1,i+1,1):
        print(y,end = '')
     
    print('')
n= 3
for i in range(1,n+1,1):
    y = n-i+n-i+i
    for j in range(1,n-i+1+1):
        print(y,end="")
    print("")
               