''' 
          1*2*3*4
          9*10*11*12
          5*6*7*8
          13*14*15*16
'''
n= 4

for i in range(1,n+1,1):
    if i%2!=0:
        y=(i-1)*4 +1
    if i%2==0:
        y=(i-2)*4+9
    for j in range(1,n+1,1):
        print(y,end='')
        if j!=n:
            print('*',end='')
        y = y+1

    print('')
