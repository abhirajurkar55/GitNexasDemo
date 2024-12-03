p=['java','python','AI','ML','Cloud','hadoop','Django']
print(p)

#update(index): it will update the value a specific index using index number we have to specify remove the old element of same index


p[3]='cloud'
print(p)

p[0]='pyhton and data science'
print(p)

# for other methods

p1=[101,1211,225252,115141,11,11,14,151,151,151,20,52,252,454,12,252,101,103,103]
print(p1)

 #index(element): it is use to find the index of element 

print(p1.index(1211))
print(p1.index(12))
print(p1.index(115141))

 #count(element):it is use to count the element in the list

print(p1.count(1211))
print(p1.count(101))
print(p1.count(151))

#reverse():it is use to reverse the list

p1.reverse()
print(p1)