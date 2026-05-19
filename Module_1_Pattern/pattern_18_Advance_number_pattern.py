'''
----1             ----*
---121            ---**+
--12321     =>    --***++
-1234321          -****+++
123454321         *****++++
'''

n=5

for i in range(1,n+1,1):
    for j in range(1,n-i+1,1):
        print(' ',end='')
    y = 1
    for j in range(1,i+1,1):
        print(y,end='')
        y=y+1
    y=i-1
    for j in range(1,i-1+1,1):
        print(y,end='')
        y-=1
    print('')
