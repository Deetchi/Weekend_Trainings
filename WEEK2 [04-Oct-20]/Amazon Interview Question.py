"""
4 October, 2020. 

Find the row and column index of the given value.

Sample Input 1:
1, 1,
[[1]], 1

Sample Output 1:
0 0

Sample Input 2:
2, 2,
[[1,2][3,4]], 3

Sample Output 2:
1 0

"""

rcvalues = list(map(str,input().split()))
rowc = rcvalues[0]
row = rowc[:1]
columnc = rcvalues[1]
col = columnc[:1]

mat_values = list(map(str,input().split(']],')))

only_values = []
for i in mat_values[0]: 
    if i == '[' or i == ']' or i == ',' or i == ' ':
        continue
    else:
        only_values.append(i)
        
matrix = []
index = 0
for i in range(int(row)):          
    row_wise_val = [] 
    for j in range(int(col)):
        row_wise_val.append(only_values[index])
        index += 1
    matrix.append(row_wise_val)

find_val = mat_values[-1]

for i in range(int(row)):
    for j in range(int(col)):
        if matrix[i][j] == find_val[-1]:
            print(i,j)
            #print('Value '+ str(find_val) + ' is present in row:' + str(i) + ' column:' + str(j))
            break
