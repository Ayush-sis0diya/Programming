'''
           1*2*3*4
           5*6*7*8
           9*10*11*12
           13*14*15*16

'''

n = 4
y = 1
for i in range(1,n+1,1):
    
    for j in range(1,n+3+1,1):
        if j%2==0:
            print('*',end='')
        else:
            print(y,end=' ')
            y = y+1
    print('')