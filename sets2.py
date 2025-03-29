# sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A.union(B)) #all elements in A and B

print(A.intersection(B)) #common elements in A and B

print(A.issubset(B)) #elements of A are in B

print(A.isdisjoint(B))  #A and B have no common elements

print(A.symmetric_difference(B)) #elements that are in A or B but not in both

print(B.union(A)) 

del A #delete the set A
del B #delete the set B

print(A)
print(B)