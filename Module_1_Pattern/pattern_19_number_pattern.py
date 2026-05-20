'''
----1
---212
--32123
-4321234
543212345
'''
n=5 
for i in range(1,n+1,1):
    for j in range(1,n-i+1,1):
        print('-',end = '')
    y = i
    for j in range(1,i+1,1):
        print(y,end='')
        y = y-1
    y = 2
    for j in range(1,i-1+1,1):
        print(y,end='')
        y=y+1
    print('')