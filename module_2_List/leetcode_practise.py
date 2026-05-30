#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

'''
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
'''
'''
a = [0,1,2,2,3,0,4,2]
v = 2

for i in range(len(a)):
    for j in range(i-1,len(a)-1):
        if a[i]==v:
            a.pop(i)
print(len(a),', nums =',a)
'''

'''
b = [1,2,3]
d = 0
for i in range(len(b)+1):
    d = d*10 + i
d = d+1
result = list(map(int, str(d)))
print(result)
'''
'''
a = [1,3,5,6]
t = 5
for i in range(len(a)):
    if a[i]==t:
        print(i)
    if t not in a:
        a.append(t)
        a.sort()
'''
'''
s = "Hello    my name is World"
a =s.strip().split(' ')
print(len(a[-1]))
'''
'''
s = "A man, a plan, a canal: Panama"
v = ""
for i in s:
    if i.isalnum():
        v +=i.lower()
if v ==v[::-1]:
    print('True')
'''
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
for i in range(len(nums1)):
    if nums1[i]==0:
       nums1[i]=nums2[i-3]
print(sorted(nums1))