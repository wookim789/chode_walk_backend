result = []
 
for i in range(65, 72):
    result.append(i)
for i in range(97, 104):
    result.append(i)
result.append(43)
result.append(45)

result.sort()
print(result)


print(ord('a'))
print(ord('A'))
print(ord('+'), ord('-'))


[43, 45, 65, 66, 67, 68, 69, 70, 71, 97, 98, 99, 100, 101, 102, 103]

A = ['A' , 'B' ,  'C+' , 'D' ,  'E' ,  'F+' , 'G+']
B = ['B' , 'C+' , 'D+' , 'E' ,  'F+' , 'G+' , 'A+']
C = ['C' , 'D' ,  'E' ,  'F' ,  'G' ,  'A' ,  'B']
D = ['D' , 'E' ,  'F+' , 'G' ,  'A' ,  'B' ,  'C+']
E = ['E' , 'F+' , 'G+' , 'A' ,  'B' ,  'C+' , 'D+']
F = ['F' , 'G' ,  'A' ,  'B-',  'C' ,  'D' ,  'E']
G = ['G' , 'A' ,  'B' ,  'C' ,  'D' ,  'E' ,  'F+']

for idx in range(7):
    A[idx] = A[idx].lower()
for idx in range(7):
    B[idx] = B[idx].lower()
for idx in range(7):
    C[idx] = C[idx].lower()
for idx in range(7):
    D[idx] = D[idx].lower()
for idx in range(7):
    E[idx] = E[idx].lower()
for idx in range(7):
    F[idx] = F[idx].lower()
for idx in range(7):
    G[idx] = G[idx].lower()

print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print(G)

test_key_list = []
for i in range(35, 128):    
    test_key_list.append(chr(i))
print(test_key_list)