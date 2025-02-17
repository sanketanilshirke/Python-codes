l=[4,2,3,1,5,1]
print(l)
l.reverse()
print(l)
l.append(9)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.insert(0,0)
l.insert(3,90)
print(l)
l.remove(9)
print(l)
l.pop(2)  
print(l)

print(l.count(1))

print(sorted(l))

#
ab=[1,2,3]
ab.extend([9,9,9,0])
print(ab)