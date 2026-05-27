#generating all the pair of an array

#approach 1
#when i=0,j=0
'''
a = [1,2,3,4,5]
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i],a[j])
    print('')
'''


#approach 2
#when i<j i.e i=0,j=i+1
'''
a = [1,2,3,4,5]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        print(a[i],a[j])
    print('')
'''


#print sum of all the pairs of i anf j
'''
a = [1,2,3,4,5]
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i],'+',a[j],'==',a[i]+a[j])
    print('')
'''

#print sum of all the pairs of i ana j but only if i<j
a = [1,2,3,4,5]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        print(a[i],'+',a[j],'==',a[i]+a[j])
    print('')

