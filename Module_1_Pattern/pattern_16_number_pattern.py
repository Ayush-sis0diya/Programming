'''
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1


'''
n = 5
for i in range(1,n+1,1):
    y = n # extra variable y
    for j in range(1,i+1,1):
        print(y,end='')
        y = y-1
    print('')