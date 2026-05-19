'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15


n = 5
y = 1
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print(y,end=' ')
        y = y+1
    print('')
'''
'''
15 
14 13 
12 11 10
9  8  7  6
5  4  3  2  1

'''
n = 5
y = 15
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print(y,end=' ')
        y-=1
    print('')