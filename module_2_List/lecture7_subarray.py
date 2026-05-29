#all sub array of an main array using brute force

a = [10,20,30,40,50,60]
'''
for i in range(len(a)):
    for j in range(i,len(a)):
        for k in range(i,j+1):
            print(a[k],end = ' ')
        print('')
'''


#sum of all the sub array 

for i in range(len(a)):
    for j in range(i,len(a)):
        sum = 0
        for k in range(i,j+1): 
            print(a[k],end = ' ')
            sum = sum+a[k]
        print("sum =",sum)
        print('')