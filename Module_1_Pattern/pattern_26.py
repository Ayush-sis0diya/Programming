n = 4
st  = 2
for i in range(1,n+1,1):
    y = st
    for j in range(1,i+1,1):
        print(y,end='')
        y=y-1
    print('')
    st = st+i+1
n=4
st2 = 11
for i in range(1,n+1,1):
    y = st2
    for j in range(1,n-i+1+1,1):
        print(y,end='')
        y = y-1
    print('')
    st2 = y
