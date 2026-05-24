#creating a list
a=[]

#adding element in list
a.append(10)
a.append(1)
a.append(2)
a.append(330)
a.append(30)
print(a) #[10, 1, 2, 330, 30]

#fetching the element
print(a[3]) #330

#deleting the element
a.pop(3)
print(a)#[10, 1, 2, 30]

#finding the largest element
print(max(a)) #30

#finding the minimum element

print(min(a)) #1

#sorting the list
print(a.sort())


#reversing the list
y = a[::-1]
print(y)