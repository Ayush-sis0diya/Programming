'''
1 1 1 1 1 1 1 1 1      * * * * * * * * *
1 2 2 2 2 2 2 2 1      1 * * * * * * * 1
1 2 3 3 3 3 3 2 1      1 2 * * * * * 2 1
1 2 3 4 4 4 3 2 1      1 2 3 * * * 3 2 1
1 2 3 4 5 4 3 2 1   => 1 2 3 4 * 4 3 2 1
1 2 3 4 4 4 3 2 1
1 2 3 3 3 3 3 2 1      1 2 3 * * * 3 2 1
1 2 2 2 2 2 2 2 1      1 2 * * * * * 2 1
1 1 1 1 1 1 1 1 1      1 * * * * * * * 1
                       * * * * * * * * *

'''
n = 5 
for i in range(1,n+1,1):
    y = 1
    for j in range(1,i-1+1,1):
        print(y,end = "")
        y = y+1
    for j in range(1,n-i+n-i+1+1,1):
        print(i,end = '')
    y = i-1
    for j in range(1,i-1+1,1):
        print(y,end = "")
        y = y-1
    print('')
n = 4
for i in range(1,n+1,1):
    y = 1
    for j in range(1,n-i+1,1):
        print(y,end = "")
        y = y+1
    y = n -i +1 
    for j in range(1,i+i+1+1,1):
        print(y,end='')
    
    y=n-i
    for j in range(1,n-i+1,1):
        print(y,end='')
        y = y-1
    
        
    print('')



   
